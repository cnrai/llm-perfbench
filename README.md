# LLM Performance Benchmark for Apple M3 Ultra

[![image](https://github.com/user-attachments/assets/6d432ee9-1186-41e6-a191-010640a87899)](https://cnr.ai)

A benchmarking tool for measuring various Large Language Model (LLM) inference performance across different runtime engines on Apple M3 Ultra hardware.

## Overview

This project provides a standardized framework for evaluating the token processing speed (both input and output) of various LLM inference engines. It focuses on measuring real-world performance on Apple M3 Ultra chips to help developers optimize their LLM deployments.

## Benchmark Methodology

### Testing Criteria

| Parameter             | Details                                                                      |
| --------------------- | ---------------------------------------------------------------------------- |
| **Hardware**          | Apple M3 Ultra (32-core CPU, 80-core GPU, 32-core Neural Engine)             |
| **RAM**               | 512GB unified memory, 819GB/s memory bandwidth                               |
| **OS**                | macOS Sequoia 15.3.2                                                         |
| **Prompt Sets**       | Short (< 100 tokens), Long (1000+ tokens)                                    |
| **Metrics Collected** | Input tokens/sec, Output tokens/sec, Memory usage                            |
| **Iterations**        | 3 runs per model/runtime configuration without warmup (avoid prompt caching) |

## Benchmark Results

Below are example results measuring tokens per second for both input tokenization and output generation across different runtime engines and models.

### Input Tokenization Speed (tokens/sec)

| Model                                    | MLX   | LM Studio | llama.cpp  |
| ---------------------------------------- | ----- | --------- | ---------- |
| DeepSeek-V3-0324-4bit                    | 41.5  | N/A       | Not tested |
| DeepSeek-R1-Q4_K_M                       | N/A   | N/A       | 12.9       |
| Mistral-Small-3.1-24B-Instruct-2503-bf16 | 234.1 | N/A       | Not tested |
| Llama-3.3-70b-instruct-fp16              | 66.0  | N/A       | Not tested |

Note: LM Studio does not provide input tokenization speed.

### Output Generation Speed (tokens/sec)

| Model                                    | MLX  | LM Studio | llama.cpp  |
| ---------------------------------------- | ---- | --------- | ---------- |
| DeepSeek-V3-0324-4bit                    | 20.9 | 19.7      | Not tested |
| DeepSeek-R1-Q4_K_M                       | N/A  | 15.9      | 15.5       |
| Mistral-Small-3.1-24B-Instruct-2503-bf16 | 15.5 | 15.6      | Not tested |
| Llama-3.3-70b-instruct-fp16              | 5.1  | 4.9       | Not tested |

Note: DeepSeek-R1-Q4_K_M cannot be tested with MLX due to the GGUF model format.

### Memory Usage (GB)

| Model                                    | MLX | LM Studio | llama.cpp  |
| ---------------------------------------- | --- | --------- | ---------- |
| DeepSeek-V3-0324-4bit                    | 381 | 354       | Not tested |
| DeepSeek-R1-Q4_K_M                       | N/A | 396       | 435        |
| Mistral-Small-3.1-24B-Instruct-2503-bf16 | 48  | 45        | Not tested |
| Llama-3.3-70b-instruct-fp16              | 141 | 132       | Not tested |

### Runtime Engines Tested

- **MLX**: MLX is an array framework for machine learning on Apple silicon by Apple. We expect it to be the fastest runtime engine for LLMs on M3 Ultra hardware.
- **LM Studio**: LM Studio is a desktop application designed to facilitate local experimentation, management, and interaction with large language models (LLMs)
- **llama.cpp**: Inference engine of Meta's LLaMA model (and others) in pure C/C++.


## Features

- Benchmark multiple LLM runtime engines (MLX, LM Studio, llama.cpp)
- Test with various model sizes (Up to 671B parameters)
- Measure both input tokenization speed and output generation speed
- Monitor hardware resource utilization (GPU, memory)
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
```

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
