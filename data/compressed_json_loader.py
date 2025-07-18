#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
压缩JSON数据加载器

功能：
1. 加载压缩JSON格式数据 (.json.gz)
2. 兼容现有的Excel加载器接口
3. 自动格式检测和转换
4. 数据验证和自检功能

作者: 267278466@qq.com
版本: 1.0.0
"""

import os
import json
import gzip
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, Any, Tuple, Optional, Union
from datetime import datetime
import logging

# 导入现有的配置
try:
    from config import RATING_SCORE_MAP, MARKET_CONFIG
except ImportError:
    RATING_SCORE_MAP = {
        '大多': 7, '中多': 6, '小多': 5, '微多': 4,
        '微空': 3, '小空': 2, '中空': 1, '大空': 0, 
        '-': None
    }
    MARKET_CONFIG = {'CN': {'name': '中国A股'}}

# 导入格式转换器
try:
    from tools.format_converter import CompressedJSONFormat
except ImportError:
    # 如果无法导入，提供基本功能
    class CompressedJSONFormat:
        def __init__(self):
            self.format_version = "1.0"
        
        def self_check(self, file_path: str) -> Dict[str, Any]:
            return {'validation_passed': True, 'message': '基本验证通过'}

logger = logging.getLogger(__name__)


class CompressedJSONLoader:
    """压缩JSON数据加载器"""
    
    def __init__(self, file_path: str):
        """
        初始化加载器
        
        Args:
            file_path: 数据文件路径（支持 .json.gz 和 .xlsx）
        """
        self.file_path = file_path
        self.data = None
        self.validation_result = {}
        self.file_info = {}
        self.load_time = None
        self.format_converter = CompressedJSONFormat()
        
    def load_and_validate(self) -> Tuple[Optional[pd.DataFrame], Dict]:
        """
        加载并验证数据
        
        Returns:
            tuple: (DataFrame对象, 验证结果字典)
        """
        start_time = datetime.now()
        
        try:
            logger.info(f"开始加载数据文件: {self.file_path}")
            
            # 1. 文件检查
            file_check = self._check_file()
            if not file_check['is_valid']:
                return None, file_check
            
            # 2. 根据文件类型加载数据
            if self.file_path.endswith('.json.gz'):
                self.data = self._load_compressed_json()
            elif self.file_path.endswith(('.xlsx', '.xls')):
                # 如果是Excel文件，先转换为压缩JSON再加载
                self.data = self._load_excel_via_conversion()
            else:
                return None, {'is_valid': False, 'error': '不支持的文件格式'}
            
            if self.data is None:
                return None, {'is_valid': False, 'error': '数据加载失败'}
            
            # 3. 数据验证
            self.validation_result = self._validate_data_structure()
            
            # 4. 数据清洗
            if self.validation_result['is_valid']:
                self.data = self._clean_data()
            
            # 5. 记录加载时间
            self.load_time = (datetime.now() - start_time).total_seconds()
            self.validation_result['load_time'] = f"{self.load_time:.2f}s"
            self.validation_result['file_info'] = self.file_info
            
            logger.info(f"数据加载完成: {self.data.shape if self.data is not None else 'Failed'}")
            
            return self.data, self.validation_result
            
        except Exception as e:
            error_msg = f"数据加载异常: {str(e)}"
            logger.error(error_msg)
            return None, {'is_valid': False, 'error': error_msg}
    
    def _check_file(self) -> Dict:
        """检查文件是否存在和可读"""
        if not os.path.exists(self.file_path):
            return {'is_valid': False, 'error': f'文件不存在: {self.file_path}'}
        
        if not os.path.isfile(self.file_path):
            return {'is_valid': False, 'error': f'不是有效文件: {self.file_path}'}
        
        # 检查文件扩展名
        _, ext = os.path.splitext(self.file_path)
        if ext.lower() not in ['.gz'] and not self.file_path.endswith('.json.gz'):
            if ext.lower() not in ['.xlsx', '.xls']:
                return {'is_valid': False, 'error': f'不支持的文件格式: {ext}'}
        
        # 获取文件信息
        file_stat = os.stat(self.file_path)
        self.file_info = {
            'file_name': os.path.basename(self.file_path),
            'file_size': file_stat.st_size,
            'file_size_mb': round(file_stat.st_size / 1024 / 1024, 2),
            'modified_time': datetime.fromtimestamp(file_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
            'format_type': 'compressed_json' if self.file_path.endswith('.json.gz') else 'excel'
        }
        
        return {'is_valid': True}
    
    def _load_compressed_json(self) -> Optional[pd.DataFrame]:
        """加载压缩JSON数据"""
        try:
            logger.info(f"正在加载压缩JSON文件: {self.file_path}")
            
            # 读取压缩JSON文件
            with gzip.open(self.file_path, 'rt', encoding='utf-8') as f:
                data_structure = json.load(f)
            
            # 验证数据结构
            validation_result = self._validate_json_structure(data_structure)
            if not validation_result['valid']:
                logger.error(f"JSON数据验证失败: {validation_result['error']}")
                return None
            
            # 重建DataFrame
            df = self._rebuild_dataframe_from_json(data_structure)
            
            logger.info(f"成功加载压缩JSON数据: {df.shape}")
            return df
            
        except Exception as e:
            logger.error(f"压缩JSON加载失败: {e}")
            return None
    
    def _load_excel_via_conversion(self) -> Optional[pd.DataFrame]:
        """通过转换加载Excel数据"""
        try:
            logger.info(f"正在通过转换加载Excel文件: {self.file_path}")
            
            # 直接读取Excel文件
            df = pd.read_excel(self.file_path)
            
            logger.info(f"成功加载Excel数据: {df.shape}")
            return df
            
        except Exception as e:
            logger.error(f"Excel加载失败: {e}")
            return None
    
    def _validate_json_structure(self, data_structure: Dict[str, Any]) -> Dict[str, Any]:
        """验证JSON数据结构"""
        try:
            # 检查必需字段
            required_fields = ['metadata', 'data', 'checksum', 'self_check']
            for field in required_fields:
                if field not in data_structure:
                    return {'valid': False, 'error': f'缺少必需字段: {field}'}
            
            # 检查格式版本
            if data_structure['metadata']['format_version'] != self.format_converter.format_version:
                return {'valid': False, 'error': '格式版本不匹配'}
            
            # 验证数据完整性
            calculated_hash = self._calculate_data_hash(data_structure['data'])
            if calculated_hash != data_structure['checksum']:
                return {'valid': False, 'error': '数据校验和不匹配'}
            
            return {'valid': True, 'message': '数据验证通过'}
            
        except Exception as e:
            return {'valid': False, 'error': f'验证过程出错: {str(e)}'}
    
    def _rebuild_dataframe_from_json(self, data_structure: Dict[str, Any]) -> pd.DataFrame:
        """从JSON数据结构重建DataFrame"""
        data_content = data_structure['data']
        columns = data_structure['metadata']['columns']
        
        # 重建DataFrame
        df = pd.DataFrame(data_content, columns=columns)
        
        # 恢复数据类型
        dtypes = data_structure['metadata']['dtypes']
        for col, dtype_str in dtypes.items():
            if col in df.columns:
                try:
                    if 'int' in dtype_str:
                        df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
                    elif 'float' in dtype_str:
                        df[col] = pd.to_numeric(df[col], errors='coerce')
                    else:
                        df[col] = df[col].astype(str)
                except Exception as e:
                    logger.warning(f"无法恢复列 {col} 的数据类型: {e}")
        
        return df
    
    def _calculate_data_hash(self, data: list) -> str:
        """计算数据校验和"""
        import hashlib
        data_str = json.dumps(data, sort_keys=True, ensure_ascii=False)
        return hashlib.md5(data_str.encode('utf-8')).hexdigest()
    
    def _validate_data_structure(self) -> Dict:
        """验证数据结构"""
        if self.data is None:
            return {'is_valid': False, 'error': '数据为空'}
        
        validation = {
            'is_valid': True,
            'missing_columns': [],
            'warnings': [],
            'data_quality': {}
        }
        
        # 检查必需列
        required_columns = ['行业', '股票代码', '股票名称']
        for col in required_columns:
            if col not in self.data.columns:
                validation['missing_columns'].append(col)
                validation['is_valid'] = False
        
        # 检查日期列
        date_columns = [col for col in self.data.columns if str(col).startswith('202')]
        
        if len(date_columns) == 0:
            validation['warnings'].append('未找到日期列')
            validation['is_valid'] = False
        elif len(date_columns) < 5:
            validation['warnings'].append('日期列过少，可能影响趋势分析准确性')
        
        # 数据质量检查
        if validation['is_valid']:
            validation['data_quality'] = {
                'total_rows': len(self.data),
                'total_columns': len(self.data.columns),
                'date_columns_count': len(date_columns),
                'date_range': f"{min(date_columns)} ~ {max(date_columns)}" if date_columns else "无",
                'industry_coverage': self.data['行业'].notna().sum() / len(self.data) * 100,
                'duplicate_codes': self.data['股票代码'].duplicated().sum(),
                'duplicate_names': self.data['股票名称'].duplicated().sum()
            }
        
        return validation
    
    def _clean_data(self) -> pd.DataFrame:
        """数据清洗"""
        df = self.data.copy()
        
        # 1. 股票代码标准化
        if '股票代码' in df.columns:
            df['股票代码'] = df['股票代码'].astype(str).str.zfill(6)
        
        # 2. 行业信息处理
        if '行业' in df.columns:
            df['行业'] = df['行业'].fillna('未分类')
            df['行业'] = df['行业'].astype(str).str.strip()
        
        # 3. 股票名称处理
        if '股票名称' in df.columns:
            df['股票名称'] = df['股票名称'].astype(str).str.strip()
        
        # 4. 评级数据处理
        date_columns = [col for col in df.columns if str(col).startswith('202')]
        for col in date_columns:
            valid_ratings = set(RATING_SCORE_MAP.keys())
            mask = ~df[col].isin(valid_ratings)
            df.loc[mask, col] = '-'
        
        logger.info(f"数据清洗完成: {len(df)} 行数据")
        return df
    
    def get_data_summary(self) -> Dict:
        """获取数据概览"""
        if self.data is None:
            return {}
        
        date_columns = [col for col in self.data.columns if str(col).startswith('202')]
        
        # 评级分布统计
        rating_stats = {}
        if date_columns:
            latest_col = max(date_columns)
            rating_dist = self.data[latest_col].value_counts()
            
            for rating, count in rating_dist.items():
                percentage = count / len(self.data) * 100
                rating_stats[rating] = {
                    'count': count,
                    'percentage': round(percentage, 1)
                }
        
        # 行业分布
        industry_stats = {}
        if '行业' in self.data.columns:
            industry_dist = self.data['行业'].value_counts()
            for industry, count in industry_dist.head(10).items():
                percentage = count / len(self.data) * 100
                industry_stats[industry] = {
                    'count': count,
                    'percentage': round(percentage, 1)
                }
        
        return {
            'total_stocks': len(self.data),
            'total_columns': len(self.data.columns),
            'date_range': f"{min(date_columns)} ~ {max(date_columns)}" if date_columns else "无",
            'trading_days': len(date_columns),
            'industry_coverage': self.data['行业'].notna().sum() / len(self.data) * 100 if '行业' in self.data.columns else 0,
            'latest_rating_stats': rating_stats,
            'top_industries': industry_stats,
            'load_time': self.load_time,
            'format_type': self.file_info.get('format_type', 'unknown')
        }


def load_data_with_format_detection(file_path: str) -> Tuple[Optional[pd.DataFrame], Dict]:
    """
    自动检测格式并加载数据
    
    Args:
        file_path: 数据文件路径
        
    Returns:
        tuple: (DataFrame, 加载结果)
    """
    loader = CompressedJSONLoader(file_path)
    return loader.load_and_validate()


def convert_excel_to_compressed_json(excel_path: str, output_path: str = None) -> Dict[str, Any]:
    """
    便捷函数：将Excel文件转换为压缩JSON格式
    
    Args:
        excel_path: Excel文件路径
        output_path: 输出文件路径
        
    Returns:
        转换结果
    """
    try:
        converter = CompressedJSONFormat()
        return converter.excel_to_compressed_json(excel_path, output_path)
    except Exception as e:
        return {'success': False, 'error': str(e)}


# 测试函数
def test_compressed_json_loader():
    """测试压缩JSON加载器"""
    print("测试压缩JSON加载器...")
    
    # 测试文件
    test_files = ["CN_Demo300.json.gz", "CN_Demo300.xlsx"]
    
    for test_file in test_files:
        if os.path.exists(test_file):
            print(f"\n正在测试文件: {test_file}")
            
            loader = CompressedJSONLoader(test_file)
            data, result = loader.load_and_validate()
            
            if result.get('is_valid', False):
                print(f"✓ 加载成功: {data.shape}")
                summary = loader.get_data_summary()
                print(f"  格式类型: {summary.get('format_type', 'unknown')}")
                print(f"  加载时间: {summary.get('load_time', 'N/A')}")
                print(f"  数据规模: {summary.get('total_stocks', 0)} 股票")
            else:
                print(f"✗ 加载失败: {result.get('error', '未知错误')}")
        else:
            print(f"测试文件不存在: {test_file}")
    
    print("\n测试完成")


if __name__ == "__main__":
    test_compressed_json_loader() 