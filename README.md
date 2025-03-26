# LLM Performance Benchmark

A comprehensive benchmarking tool for measuring Large Language Model (LLM) inference performance across different runtime engines on Apple M3 Ultra hardware.

## Overview

This project provides a standardized framework for evaluating the token processing speed (both input and output) of various LLM inference engines. It focuses on measuring real-world performance on Apple M3 Ultra chips to help developers optimize their LLM deployments.

## Features

- Benchmark multiple LLM runtime engines (Ollama, LM Studio, etc.)
- Test with various model sizes (7B to 671B parameters)
- Measure both input tokenization speed and output generation speed
- Monitor hardware resource utilization (CPU, memory, GPU)
- Generate detailed performance reports and visualizations

## Installation

```bash
# Clone the repository
git clone https://github.com/cnrai/llm-perfbench.git
cd llm-perfbench

# Install dependencies
python -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Test the installation
python3 src/hardware/hardware_info.py
```

## Usage

```bash
# Run benchmark with default settings
python main.py

# Run benchmark for a specific runtime and model
python main.py --runtime ollama --model llama3:8b

# Use different prompt lengths
python main.py --prompt-set short
python main.py --prompt-set medium
python main.py --prompt-set long
```

## Benchmark Methodology

### Testing Criteria

| Parameter | Details |
|-----------|---------|
| **Hardware** | Apple M3 Ultra (32-core CPU, 80-core GPU, 32-core Neural Engine) |
| **RAM** | 512GB unified memory, 819GB/s memory bandwidth |
| **OS** | macOS Sequoia 15.3 (24D2059) |
| **Prompt Sets** | Short (< 100 tokens), Medium (100-1000 tokens), Long (1000+ tokens) |
| **Metrics Collected** | Input tokens/sec, Output tokens/sec, Total latency, CPU usage, Memory usage, GPU utilization |
| **Iterations** | 3 runs per model/runtime configuration with warmup |

### Runtime Engines Tested

- **Ollama**: Ollama is an open-source tool that allows you to run LLMs locally on your machine
- **LM Studio**: LM Studio is a desktop application designed to facilitate local experimentation, management, and interaction with large language models (LLMs)


## Benchmark Results

Below are example results measuring tokens per second for both input tokenization and output generation across different runtime engines and models.

### Input Tokenization Speed (tokens/sec)

| Model         | Ollama | LM Studio |
|---------------|--------|-----------|
| Llama-3 8B    | TBD    | TBD       |
| Llama-3 70B   | TBD    | TBD       |
| Mistral 7B    | TBD    | TBD       |
| Phi-3 Mini    | TBD    | TBD       |
| Gemma 7B      | TBD    | TBD       |

### Output Generation Speed (tokens/sec)

| Model         | Ollama | LM Studio |
|---------------|--------|-----------|
| Llama-3 8B    | TBD    | TBD       |
| Llama-3 70B   | TBD    | TBD       |
| Mistral 7B    | TBD    | TBD       |
| Phi-3 Mini    | TBD    | TBD       |
| Gemma 7B      | TBD    | TBD       |

### Memory Usage (GB)

| Model         | Ollama | LM Studio |
|---------------|--------|-----------|
| Llama-3 8B    | TBD    | TBD       |
| Llama-3 70B   | TBD    | TBD       |
| Mistral 7B    | TBD    | TBD       |
| Phi-3 Mini    | TBD    | TBD       |
| Gemma 7B      | TBD    | TBD       |

## Hardware Utilization Comparison

*This section will contain charts showing CPU, memory and GPU utilization across different runtimes and models once benchmark results are collected.*

## Interpreting Results

When evaluating the results, consider:

1. **Input Processing Speed**: Faster tokenization means quicker response to user input
2. **Output Generation Speed**: Higher tokens/sec means less user waiting for model responses
3. **Memory Efficiency**: Lower memory usage allows for larger models or concurrent instances
4. **Hardware Utilization**: How efficiently each runtime uses the M3 Ultra's resources
5. **Model Size Impact**: How performance scales with different model sizes

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
