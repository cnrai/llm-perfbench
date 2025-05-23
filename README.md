<div align="center">
  
  # LLM Performance Benchmark for Apple M3 Ultra

[![image](https://github.com/user-attachments/assets/6d432ee9-1186-41e6-a191-010640a87899)](https://cnr.ai)

![output](https://github.com/user-attachments/assets/eb5f3f50-2b43-40d4-a156-59d1fc442f6e)
Running DeepSeek-V3-0324-4bit on Apple M3 Ultra 512GB - 21.4 tokens per second
</div>
<div>&nbsp;</div>

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
| Llama-3.3-70b-instruct-fp16              | 66.0  | N/A       | Not tested |
| Mistral-Small-3.1-24B-Instruct-2503-bf16 | 234.1 | N/A       | Not tested |
| DeepSeek-V3-0324-4bit                    | 114.6 | N/A       | Not tested |
| DeepSeek-R1-Q4_K_M                       | N/A   | N/A       | 12.9       |
| QwQ-32B-8bit                             | 93.8  | N/A       | Not tested |
| Qwen2.5-72B-Instruct-8bit                | 162.6 | N/A       | Not tested |
| Qwen2.5-72B-Instruct-4bit                | 163.6 | N/A       | Not tested |
| Qwen2.5-VL-32B-Instruct-8bit             | 309.4 | N/A       | Not tested |

Note:
- LM Studio does not provide input tokenization speed.
- For DeepSeek-V3-0324-4bit, this [commit](https://github.com/ml-explore/mlx-lm/tree/191d81d1a0b158f2ef0b07f9fcbc8ee561297bab) was used for MLX testing.

### Output Generation Speed (tokens/sec)

| Model                                    | MLX  | LM Studio  | llama.cpp  |
| ---------------------------------------- | ---- | ---------- | ---------- |
| Llama-3.3-70b-instruct-fp16              | 5.1  | 4.9        | Not tested |
| Mistral-Small-3.1-24B-Instruct-2503-bf16 | 15.5 | 15.6       | Not tested |
| DeepSeek-V3-0324-4bit                    | 20.9 | 19.7       | Not tested |
| DeepSeek-R1-Q4_K_M                       | N/A  | 15.9       | 15.5       |
| QwQ-32B-8bit                             | 18.2 | 18.1       | Not tested |
| Qwen2.5-72B-Instruct-8bit                | 9.3  | 8.4        | Not tested |
| Qwen2.5-72B-Instruct-4bit                | 16.7 | Not tested | Not tested |
| Qwen2.5-VL-32B-Instruct-8bit             | 18.5 | 18.7       | Not tested |

Note: DeepSeek-R1-Q4_K_M cannot be tested with MLX due to the GGUF model format.

### Memory Usage (GB)

| Model                                    | MLX | LM Studio  | llama.cpp  |
| ---------------------------------------- | --- | ---------- | ---------- |
| Llama-3.3-70b-instruct-fp16              | 141 | 132        | Not tested |
| Mistral-Small-3.1-24B-Instruct-2503-bf16 | 48  | 45         | Not tested |
| DeepSeek-V3-0324-4bit                    | 381 | 354        | Not tested |
| DeepSeek-R1-Q4_K_M                       | N/A | 396        | 435        |
| QwQ-32B-8bit                             | 35  | 34         | Not tested |
| Qwen2.5-72B-Instruct-8bit                | 79  | 73         | Not tested |
| Qwen2.5-72B-Instruct-4bit                | 42  | Not tested | Not tested |
| Qwen2.5-VL-32B-Instruct-8bit             | 38  | 36         | Not tested |

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
