# Home Energy Multi-Agent Assistant

## Overview

This project implements a multi-agent AI system for analyzing smart home electricity consumption data.

The application combines:
- data analytics
- visualization
- recommendation systems
- agent orchestration
- interactive Streamlit deployment

Users can upload a home energy consumption dataset and ask analytical questions in natural language. Specialized AI 
agents collaborate to generate insights, charts, and energy-saving recommendations.

---

# Architecture

```text
User Question
      ↓
Orchestrator Agent
      ↓
 ┌─────────────────────────────┐
 │ Analytics Agent             │
 │ Visualization Agent         │
 │ Recommendation Agent        │
 └─────────────────────────────┘
      ↓
Combined Results
      ↓
Streamlit Interface
```

---

# Features

- ⚡ Smart home electricity consumption analysis
- 🤖 Multi-agent orchestration architecture
- 📊 Interactive visualizations using Plotly
- 📈 Time-series and appliance-level analytics
- 💡 Energy-saving recommendations
- 🌐 Interactive Streamlit web application
- 📁 CSV upload support
- ⚙️ Modular and extensible project structure

---

# Agent System

## Orchestrator Agent
Routes user questions to the appropriate specialized agents.

## Analytics Agent
Handles:
- total consumption
- average consumption
- appliance rankings
- cost estimation
- seasonal analysis

## Visualization Agent
Generates:
- appliance consumption charts
- seasonal consumption charts
- time-series visualizations
- temperature vs consumption analysis
- regression trend visualizations

## Recommendation Agent
Provides:
- energy optimization recommendations
- appliance efficiency insights
- cost reduction suggestions

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/erichadjakossa/home-energy-agent-assistant.git
cd home-energy-agent-assistant
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Dataset

This project uses the following dataset:

Smart Home Energy Consumption Dataset  
Source: Kaggle

Place the dataset inside the `data/` folder:

```text
data/smart_home_energy_consumption_large.csv
```

---

# Usage

## Run the Streamlit application

```bash
streamlit run app.py
```

---

# Example Questions

```text
Which appliances consume the most electricity?
```

```text
Show me the consumption trend over time.
```

```text
Show me the temperature versus consumption plot.
```

```text
What recommendations can you give me to reduce electricity consumption?
```

```text
Estimate the electricity bill.
```

---

# Visualizations

The Visualization Agent can generate:
- appliance consumption charts
- seasonal analysis charts
- household-size consumption plots
- time-series energy trends
- temperature vs consumption scatter plots with regression trendlines

---

# Project Structure

```text
home-energy-agent-assistant/
│
├── data/
│   └── smart_home_energy_consumption_large.csv
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   └── data_loader.py
│
├── tools/
│   ├── __init__.py
│   ├── analytics_tools.py
│   └── visualization_tools.py
│
├── agents/
│   ├── __init__.py
│   ├── analytics_agent.py
│   ├── visualization_agent.py
│   ├── recommendation_agent.py
│   └── orchestrator_agent.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Tech Stack

- Python
- pandas
- NumPy
- Plotly
- Streamlit
- OpenAI API
- statsmodels

---

# Motivation

This project explores how agent orchestration systems can be applied to structured energy consumption datasets.

The objective is to build AI systems capable of:
- analytical reasoning
- tool usage
- visualization generation
- recommendation synthesis
- interactive decision support

---
## Live Demo

https://home-energy-agent-assistant-eric-adjakossa.streamlit.app/
---

# Future Improvements

- LLM-based autonomous orchestration
- Memory-enabled conversational agents
- Multi-file analysis
- Advanced forecasting agents
- Appliance anomaly detection
- Real-time IoT integration
- LangGraph integration
- Deployment with authentication

---

# Author

Eric Adjakossa  
PhD in Applied Statistics | Data Scientist

