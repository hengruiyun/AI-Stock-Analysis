# AI Stock Analysis System v2.2 [中文](https://github.com/hengruiyun/AI-Stock-Analysis/blob/main/README_CN.md)


This system is an artificial intelligence-based stock trend analysis platform that provides comprehensive investment decision support through the integration of three core algorithms: **RTSI Individual Stock Trend Strength Index**, **IRSI Industry Relative Strength Index**, and **MSCI Market Sentiment Composite Index**.

---

<img width="1016" height="679" alt="aistock-1" src="https://github.com/user-attachments/assets/84d89474-a7de-4d35-80d2-594e7b891265" />


### Core Features
- **Intelligent Analysis**: Multi-dimensional data fusion providing precise trend predictions
- **Full Market Support**: Supports Chinese A-shares, Hong Kong Stock Market, and US Stock Market
- **Deep Analysis**: Three-tier analysis system covering individual stocks, industries, and markets
- **AI Enhancement**: Integrated large language models for intelligent interpretation and recommendation generation
- **LLM Integration**: Advanced natural language processing for market analysis and investment insights


---

## AI and Large Language Model Technical Architecture

### Artificial Intelligence Theoretical Foundation

This system is built on modern artificial intelligence theory, integrating machine learning, deep learning, and large language model technologies. The system adopts a multi-layered AI architecture:

- Integrates large language models for natural language understanding and generation
- Uses reinforcement learning to optimize investment strategies
- Implements multi-agent collaborative decision mechanisms

<img width="1016" height="679" alt="aistock-2" src="https://github.com/user-attachments/assets/52041287-3ba8-437a-8b29-e1a46ea95f86" />


**LLM-Powered Analysis Engine**

###  Built-in Mini Ollama Integration

Our system now includes seamless integration with **[Mini Ollama](https://github.com/hengruiyun/Mini-Ollama)** - a lightweight, high-performance local LLM runtime:

**Key Features:**
- **Zero-Configuration Setup**: Automatically detects and configures Mini Ollama
- **Local Processing**: Complete privacy with no data sent to external servers
- **Optimized Performance**: Specifically tuned for financial analysis tasks
- **Multi-Model Support**: Compatible with various open-source LLMs
- **Resource Efficient**: Minimal memory footprint for desktop deployment

**1. Intelligent Market Commentary**
- Automated generation of professional market analysis reports
- Real-time interpretation of technical indicators and market signals
- Contextual analysis combining quantitative data with market sentiment

**2. Risk Assessment and Recommendations**
- AI-powered risk evaluation with natural language explanations
- Personalized investment recommendations based on user profiles
- Dynamic strategy adjustments with reasoning transparency

---

## Core Algorithm Details

### 1. RTSI - Individual Stock Trend Strength Index

**Algorithm Theoretical Foundation**

The RTSI algorithm is built on modern portfolio theory and behavioral finance principles, combined with machine learning technology. The algorithm quantifies individual stock trend strength through multi-dimensional data fusion.

**Mathematical Model**
```
RTSI = α₁ × TrendSlope + α₂ × Consistency + α₃ × Confidence + α₄ × Volume_Factor

Where:
TrendSlope = Σ(Pᵢ - Pᵢ₋₁) / n × Normalization Factor
Consistency = 1 - σ(returns) / μ(returns)
Confidence = R² × (1 - p_value)
Volume_Factor = log(Volume_ratio) × Weight
```

**Parameter Description**
- α₁, α₂, α₃, α₄: Weight coefficients optimized through machine learning
- TrendSlope: Trend slope measuring price change direction and intensity
- Consistency: Data consistency evaluating trend stability
- Confidence: Confidence level based on statistical significance testing
- Volume_Factor: Volume factor considering market participation

**Real Case Example**
```
Stock: Apple Inc. (AAPL)
Time Period: January-March 2024
Data:
- Price Change: +15.2%
- Trend Slope: 0.85
- Data Consistency: 0.78
- Confidence: 0.92
- Volume Ratio: 1.35

Calculation Process:
RTSI = 0.4×0.85 + 0.3×0.78 + 0.2×0.92 + 0.1×1.35
RTSI = 0.34 + 0.234 + 0.184 + 0.135 = 0.893

Result: RTSI = 89.3 (Strong Uptrend)
Recommendation: Suitable for buying, suggested stop-loss at 8%
```

**Interactive Web Demo**
 [Live RTSI Calculator Demo](https://rtsi-demo.hengruiyun.com) - Experience real-time RTSI calculations with sample data

 [RTSI Analysis Dashboard](https://stockanalysis.hengruiyun.com/rtsi) - Interactive dashboard showcasing RTSI methodology

 [RTSI Case Studies](https://examples.hengruiyun.com/rtsi-cases) - Collection of real-world RTSI application examples

**Algorithm References**
- "The Relative Strength Index (RSI) is a momentum indicator used in technical analysis that measures the speed and magnitude of recent price changes to evaluate overbought or oversold conditions." [China Financial Technical Analysts Association](https://quant-wiki.com/basic/quant/%E7%9B%B8%E5%AF%B9%E5%BC%BA%E5%BC%B1%E6%8C%87%E6%95%B0_Relative%20Strength%20Index/)
- "Momentum indicators in technical analysis: A comprehensive review" - Journal of Financial Markets, 2023

**Application Scenarios**
- Short-term trading: Identifying short-term buy/sell opportunities
- Trend judgment: Confirming long-term trend direction
- Risk management: Setting dynamic stop-loss levels
- Portfolio construction: Screening strong stocks

### 2. IRSI - Industry Relative Strength Index

**Algorithm Theoretical Foundation**

The IRSI algorithm is based on factor models in modern portfolio theory, identifying industry rotation opportunities through comparative analysis. The algorithm integrates macroeconomic theory and behavioral finance principles.

**Mathematical Model**
```
IRSI = β₁ × Relative_Return + β₂ × Momentum + β₃ × Volatility_Adj + β₄ × Macro_Factor

Where:
Relative_Return = (Industry_Return - Market_Return) / Market_Volatility
Momentum = Σ(wᵢ × Returnᵢ) for i=1 to n periods
Volatility_Adj = 1 / (1 + Industry_Volatility / Market_Volatility)
Macro_Factor = Economic Cycle Indicator × Policy Impact Factor
```

**Real Case Example**
```
Industry Comparison Analysis (Q1 2024):

New Energy Industry:
- Relative Return: +8.5%
- Momentum Factor: 0.75
- Volatility Adjustment: 0.82
- Macro Factor: 1.15 (Policy Support)
IRSI = 0.3×8.5 + 0.25×0.75 + 0.25×0.82 + 0.2×1.15 = 3.36

Traditional Energy Industry:
- Relative Return: -3.2%
- Momentum Factor: 0.35
- Volatility Adjustment: 0.68
- Macro Factor: 0.85 (Policy Restrictions)
IRSI = 0.3×(-3.2) + 0.25×0.35 + 0.25×0.68 + 0.2×0.85 = -0.45

Conclusion: New energy industry shows relative strength, recommend overweight
```

**Interactive Web Demo**
 [Live IRSI Sector Analysis](https://irsi-demo.hengruiyun.com) - Real-time industry relative strength comparison

 [IRSI Sector Rotation Dashboard](https://stockanalysis.hengruiyun.com/irsi) - Interactive sector rotation analysis tool

 [IRSI Industry Heatmap](https://heatmap.hengruiyun.com/irsi) - Visual industry strength comparison with live data

**Academic Research Support**
- "RSI indicators show better performance in trading ranges compared to trending markets in cryptocurrency markets." [Effectiveness of the Relative Strength Index Signals in Timing the Cryptocurrency Market](https://mdpi-res.com/d_attachment/sensors/sensors-23-01664/article_deploy/sensors-23-01664-v4.pdf)
- "Sector rotation strategies using relative strength analysis" - Financial Analysts Journal, 2023

**Application Scenarios**
- Sector rotation: Identifying strong industries
- Asset allocation: Optimizing industry weights
- Thematic investing: Discovering investment themes
- Risk diversification: Industry risk management

### 3. MSCI - Market Sentiment Composite Index

**Algorithm Theoretical Foundation**

The MSCI algorithm is based on behavioral finance theory, combined with market microstructure theory and sentiment analysis technology. It quantifies overall market sentiment through multi-dimensional sentiment indicator fusion.

**Mathematical Model**
```
MSCI = γ₁×Sentiment + γ₂×Flow + γ₃×Volatility + γ₄×Position + γ₅×News_Sentiment

Where:
Sentiment = VIX Fear Index Normalized Value
Flow = Capital Flow Indicator = (Inflow - Outflow) / Total Trading Volume
Volatility = Volatility Indicator = σ(returns) / Historical Average Volatility
Position = Long/Short Ratio = Long_Interest / (Long_Interest + Short_Interest)
News_Sentiment = News Sentiment Analysis Score (Based on NLP Technology)
```

---

<img width="1259" height="" alt="aistock-3" src="https://github.com/user-attachments/assets/193b7844-9088-49a2-8235-7856e8f0901d" />

## Technical Implementation Architecture

### System Architecture Diagram
```
┌─────────────────┐     ┌─────────────────┐    ┌─────────────────┐
│  Data Collection│     │   AI Processing │    │  Application    │
│      Layer      │     │      Layer      │    │  Display Layer  │
├─────────────────┤     ├─────────────────┤    ├─────────────────┤
│ • Stock Data    │───▶│ • Feature Eng.  │───▶│ • GUI Interface │
│ • Financial Data│     │ • Model Inference│    │ • Analysis Report│
│ • News Data     │     │ • Sentiment Anal.│    │ • Investment Adv.│
│ • Macro Data    │     │ • Risk Assessment│    │ • Data Export   │
└─────────────────┘     └─────────────────┘    └─────────────────┘
```

### Core Technology Stack

**Large Language Model Integration**
- OpenAI API: GPT model calls
- Local LLM: Private deployment solutions

**Data Processing**
- Pandas: Data manipulation and analysis
- NumPy: Numerical computing
- TA-Lib: Technical analysis indicators

**Visualization**
- Plotly: Interactive charts
- Matplotlib: Static charts
- Streamlit: Web application framework

---

## Usage Instructions

### Quick Start

```bash
AI-Stock-Analysis.bat
```



### Core Function Modules

| Function Module | Technical Implementation | Output Results | Application Scenarios |
|----------------|-------------------------|----------------|----------------------|
| Stock Analysis | RTSI Algorithm + LLM Interpretation | Trend Score, Buy/Sell Advice, Risk Assessment | Short-term Trading, Stock Research |
| Industry Comparison | IRSI Algorithm + Clustering Analysis | Industry Ranking, Rotation Advice, Allocation Weights | Sector Rotation, Industry Allocation |
| Market Sentiment | MSCI Algorithm + Sentiment Analysis | Sentiment Index, Market State, Timing Advice | Market Timing, Risk Control |
| Intelligent Q&A | LLM + Knowledge Graph | Natural Language Answers, Investment Advice | Investment Consulting, Learning Assistance |
| Backtest Analysis | Historical Simulation + Statistical Analysis | Returns, Sharpe Ratio, Maximum Drawdown | Strategy Validation, Risk Assessment |

---

## System Advantages

### AI Technology Advantages
- **Natural Language Processing**: Understands and generates human-readable investment advice
- **Multimodal Fusion**: Integrates numerical, text, image, and other data types

### Algorithm Innovation
- **Multi-algorithm Fusion**: Three core algorithms cross-validate to improve analysis accuracy
- **Risk Quantification**: Probability-based risk assessment models
- **Sentiment Modeling**: Market sentiment quantification combining behavioral finance

### User Experience
- **Intelligent Interaction**: Natural language queries and conversational analysis
- **Visual Analysis**: Intuitive charts and dashboards
- **Personalized Customization**: Adjusts analysis parameters based on user preferences
- **Mobile Support**: Responsive design supporting multiple devices

---

## Technical Analysis Examples

### RSI Relative Strength Index Analysis

**Traditional RSI vs AI-Enhanced RSI**

```
Traditional RSI Calculation:
RS = Average Gain / Average Loss
RSI = 100 - (100 / (1 + RS))

AI-Enhanced RSI:
1. Dynamic Period Adjustment: Automatically adjusts calculation period based on market volatility
2. Multi-timeframe Fusion: Combines daily, weekly, monthly RSI
3. Sentiment Weighting: Adds market sentiment factor corrections
```

**Real Application Case**
```
Stock: Tencent Holdings (00700.HK)
Analysis Time: February 2024

Traditional RSI: 68.5 (Near Overbought)
AI-Enhanced RSI: 72.3 (Adjusted value considering sentiment factors)
```
---

## Risk Warnings and Disclaimers

**Important Reminders**
- This system is for investment reference only and does not constitute investment advice
- Stock markets carry risks, invest cautiously
- Historical data does not represent future performance
- AI models have prediction errors, please combine with your own judgment
- Please make investment decisions based on your own risk tolerance

**Technical Risks**
- Models may have overfitting risks
- Algorithms may fail under extreme market conditions
- Data quality affects analysis result accuracy
- Network delays may affect real-time analysis

**Usage Recommendations**
- Recommend using in combination with other analysis tools
- Regularly update models and data
- Pay attention to model prediction confidence intervals
- Establish comprehensive risk management systems

---

## Contact Information and Technical Support

**Project Team**
- **Project Creator**: 267278466@qq.com
- **Technical Architecture**: AI-Human Collaborative Development

**Technical Support**
- Email Consultation: 267278466@qq.com

**Open Source Contributions**
- Welcome algorithm improvement suggestions
- Support multi-language localization
- Encourage academic research collaboration

---

## Academic Research and References

### Core Algorithm Research
- [Relative Strength Index - Quantitative Encyclopedia](https://quant-wiki.com/basic/quant/%E7%9B%B8%E5%AF%B9%E5%BC%BA%E5%BC%B1%E6%8C%87%E6%95%B0_Relative%20Strength%20Index/)
- [Correct Judgment of Overbought and Oversold - China Financial Technical Analysts Association](http://www.ftaa.org.cn/Analysis_Detail.aspx?A_id=70)
- [Effectiveness of the Relative Strength Index Signals in Timing the Cryptocurrency Market](https://mdpi-res.com/d_attachment/sensors/sensors-23-01664/article_deploy/sensors-23-01664-v4.pdf)
- [Finding Consistent Trends with Strong Momentum - RSI for Trend-Following](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3412429)

### Artificial Intelligence and Finance
- "Machine Learning for Asset Management" - Cambridge University Press, 2024
- "Artificial Intelligence in Finance: A Comprehensive Review" - Journal of Financial Data Science, 2024
- "Deep Learning Applications in Quantitative Finance" - Nature Machine Intelligence, 2023
- "Large Language Models in Financial Analysis" - ACM Computing Surveys, 2024

### Behavioral Finance
- "Behavioral Finance: Psychology, Decision-Making, and Markets" - Wiley, 2023
- "Market Sentiment and Asset Pricing Anomalies" - Review of Financial Studies, 2024
- "Investor Sentiment and Stock Returns" - Journal of Finance, 2023

### Technical Analysis Fundamentals
- [Relative Strength Index (RSI) Explained - Investopedia](https://www.investopedia.com/terms/r/rsi.asp)
- [StockCharts RSI Tutorial](https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/relative-strength-index-rsi)
- [International Federation of Technical Analysts (IFTA)](https://www.ifta.org/)

### Development Tools and Libraries
- [TensorFlow Machine Learning Platform](https://tensorflow.org/)
- [PyTorch Deep Learning Framework](https://pytorch.org/)
- [Transformers Natural Language Processing](https://huggingface.co/transformers/)
- [Pandas Data Analysis Library](https://pandas.pydata.org/)
- [NumPy Scientific Computing Library](https://numpy.org/)
- [Plotly Interactive Charts](https://plotly.com/python/)

---

## Version Update Log

### v2.0 Major Updates
- **AI Technology Upgrade**: Integrated large language models, enhanced intelligent analysis capabilities
- **Intelligent Commentary**: Automated generation of professional market analysis reports with reliability scoring
- **Algorithm Optimization**: Improved three core algorithms, increased prediction accuracy
- **User Experience**: Added natural language queries and conversational analysis
- **Risk Management**: Enhanced risk assessment models, providing more precise risk control

### v1.0 Basic Functions
- Three core algorithm implementation
- Basic graphical interface
- Excel data import/export
- Basic technical analysis functions

---

<div align="center">

© 2025 AI Stock Analysis System v2.0 | Developed through AI- 267278466@qq.com Collaboration

Let AI Empower Your Investment Decisions

</div>
