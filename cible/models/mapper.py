# Copyright 2023-present Daniel Han-Chen & the Cible team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = [
    "INT_TO_FLOAT_MAPPER",
    "FLOAT_TO_INT_MAPPER",
]

__INT_TO_FLOAT_MAPPER = \
{
    "cible/mistral-7b-bnb-4bit" : (
        "cible/mistral-7b",
        "mistralai/Mistral-7B-v0.1",
    ),
    "cible/llama-2-7b-bnb-4bit" : (
        "cible/llama-2-7b",
        "meta-llama/Llama-2-7b-hf",
    ),
    "cible/llama-2-13b-bnb-4bit" : (
        "cible/llama-2-13b",
        "meta-llama/Llama-2-13b-hf",
    ),
    "cible/codellama-34b-bnb-4bit" : (
        "codellama/CodeLlama-34b-hf",
    ),
    "cible/zephyr-sft-bnb-4bit" : (
        "cible/zephyr-sft",
        "HuggingFaceH4/mistral-7b-sft-beta",
    ),
    "cible/tinyllama-bnb-4bit" : (
        "cible/tinyllama",
        "TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T",
    ),
    "cible/tinyllama-chat-bnb-4bit" : (
        "cible/tinyllama-chat",
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    ),
    "cible/mistral-7b-instruct-v0.1-bnb-4bit" : (
        "cible/mistral-7b-instruct-v0.1",
        "mistralai/Mistral-7B-Instruct-v0.1",
    ),
    "cible/mistral-7b-instruct-v0.2-bnb-4bit" : (
        "cible/mistral-7b-instruct-v0.2",
        "mistralai/Mistral-7B-Instruct-v0.2",
    ),
    "cible/llama-2-7b-chat-bnb-4bit" : (
        "cible/llama-2-7b-chat",
        "meta-llama/Llama-2-7b-chat-hf",
    ),
    "cible/llama-2-7b-chat-bnb-4bit" : (
        "cible/llama-2-7b-chat",
        "meta-llama/Llama-2-7b-chat-hf",
    ),
    "cible/codellama-7b-bnb-4bit" : (
        "cible/codellama-7b",
        "codellama/CodeLlama-7b-hf",
    ),
    "cible/codellama-13b-bnb-4bit" : (
        "codellama/CodeLlama-13b-hf",
    ),
    "cible/yi-6b-bnb-4bit" : (
        "cible/yi-6b",
        "01-ai/Yi-6B",
    ),
    "cible/solar-10.7b-bnb-4bit" : (
        "upstage/SOLAR-10.7B-v1.0",
    ),
    "cible/gemma-7b-bnb-4bit" : (
        "cible/gemma-7b",
        "google/gemma-7b",
    ),
    "cible/gemma-2b-bnb-4bit" : (
        "cible/gemma-2b",
        "google/gemma-2b",
    ),
    "cible/gemma-7b-it-bnb-4bit" : (
        "cible/gemma-7b-it",
        "google/gemma-7b-it",
    ),
    "cible/gemma-2b-bnb-4bit" : (
        "cible/gemma-2b-it",
        "google/gemma-2b-it",
    ),
    "cible/mistral-7b-v0.2-bnb-4bit" : (
        "cible/mistral-7b-v0.2",
        "alpindale/Mistral-7B-v0.2-hf",
    ),
    "cible/gemma-1.1-2b-it-bnb-4bit" : (
        "cible/gemma-1.1-2b-it",
        "google/gemma-1.1-2b-it",
    ),
    "cible/gemma-1.1-7b-it-bnb-4bit" : (
        "cible/gemma-1.1-7b-it",
        "google/gemma-1.1-7b-it",
    ),
    "cible/Starling-LM-7B-beta-bnb-4bit" : (
        "cible/Starling-LM-7B-beta",
        "Nexusflow/Starling-LM-7B-beta",
    ),
    "cible/Hermes-2-Pro-Mistral-7B-bnb-4bit" : (
        "cible/Hermes-2-Pro-Mistral-7B",
        "NousResearch/Hermes-2-Pro-Mistral-7B",
    ),
    "cible/OpenHermes-2.5-Mistral-7B-bnb-4bit" : (
        "cible/OpenHermes-2.5-Mistral-7B",
        "teknium/OpenHermes-2.5-Mistral-7B",
    ),
    "cible/codegemma-2b-bnb-4bit" : (
        "cible/codegemma-2b",
        "google/codegemma-2b",
    ),
    "cible/codegemma-7b-bnb-4bit" : (
        "cible/codegemma-7b",
        "google/codegemma-7b",
    ),
    "cible/codegemma-7b-it-bnb-4bit" : (
        "cible/codegemma-7b-it",
        "google/codegemma-7b-it",
    ),
    "cible/llama-3-8b-bnb-4bit" : (
        "cible/llama-3-8b",
        "meta-llama/Meta-Llama-3-8B",
    ),
    "cible/llama-3-8b-Instruct-bnb-4bit" : (
        "cible/llama-3-8b-Instruct",
        "meta-llama/Meta-Llama-3-8B-Instruct",
    ),
    "cible/llama-3-70b-bnb-4bit" : (
        "meta-llama/Meta-Llama-3-70B",
    ),
    "cible/llama-3-70b-Instruct-bnb-4bit" : (
        "meta-llama/Meta-Llama-3-70B-Instruct",
    ),
    "cible/Phi-3-mini-4k-instruct-bnb-4bit" : (
        "cible/Phi-3-mini-4k-instruct",
        "microsoft/Phi-3-mini-4k-instruct",
    ),
    "cible/mistral-7b-v0.3-bnb-4bit" : (
        "cible/mistral-7b-v0.3",
        "mistralai/Mistral-7B-v0.3",
    ),
    "cible/mistral-7b-instruct-v0.3-bnb-4bit" : (
        "cible/mistral-7b-instruct-v0.3",
        "mistralai/Mistral-7B-Instruct-v0.3",
    ),
    "cible/Phi-3-medium-4k-instruct-bnb-4bit" : (
        "cible/Phi-3-medium-4k-instruct",
        "microsoft/Phi-3-medium-4k-instruct",
    ),
    "cible/Qwen2-0.5B-bnb-4bit" : (
        "cible/Qwen2-0.5B",
        "Qwen/Qwen2-0.5B",
    ),
    "cible/Qwen2-0.5B-Instruct-bnb-4bit" : (
        "cible/Qwen2-0.5B-Instruct",
        "Qwen/Qwen2-0.5B-Instruct",
    ),
    "cible/Qwen2-1.5B-bnb-4bit" : (
        "cible/Qwen2-1.5B",
        "Qwen/Qwen2-1.5B",
    ),
    "cible/Qwen2-1.5B-Instruct-bnb-4bit" : (
        "cible/Qwen2-1.5B-Instruct",
        "Qwen/Qwen2-1.5B-Instruct",
    ),
    "cible/Qwen2-7B-bnb-4bit" : (
        "cible/Qwen2-7B",
        "Qwen/Qwen2-7B",
    ),
    "cible/Qwen2-7B-Instruct-bnb-4bit" : (
        "cible/Qwen2-7B-Instruct",
        "Qwen/Qwen2-7B-Instruct",
    ),
    "cible/Qwen2-70B-bnb-4bit" : (
        "Qwen/Qwen2-70B",
    ),
    "cible/Qwen2-70B-Instruct-bnb-4bit" : (
        "Qwen/Qwen2-70B-Instruct",
    ),
    "mistralai/Codestral-22B-v0.1" : (
        "mistral-community/Codestral-22B-v0.1",
    ),
    "cible/gemma-2-9b-bnb-4bit" : (
        "cible/gemma-2-9b",
        "google/gemma-2-9b",
    ),
    "cible/gemma-2-27b-bnb-4bit" : (
        "cible/gemma-2-27b",
        "google/gemma-2-27b",
    ),
    "cible/gemma-2-9b-it-bnb-4bit" : (
        "cible/gemma-2-9b-it",
        "google/gemma-2-9b-it",
    ),
    "cible/gemma-2-27b-it-bnb-4bit" : (
        "cible/gemma-2-27b-it",
        "google/gemma-2-27b-it",
    ),
    "cible/Phi-3-mini-4k-instruct-v0-bnb-4bit" : ( # Old Phi pre July
        "cible/Phi-3-mini-4k-instruct-v0",
    ),
    "cible/Mistral-Nemo-Instruct-2407-bnb-4bit" : ( # New 12b Mistral models
        "cible/Mistral-Nemo-Instruct-2407",
        "mistralai/Mistral-Nemo-Instruct-2407",
    ),
    "cible/Mistral-Nemo-Base-2407-bnb-4bit" : ( # New 12b Mistral models
        "cible/Mistral-Nemo-Base-2407",
        "mistralai/Mistral-Nemo-Base-2407",
    ),
    "cible/Meta-Llama-3.1-8B-bnb-4bit" : (
        "cible/Meta-Llama-3.1-8B",
        "meta-llama/Meta-Llama-3.1-8B",
    ),
    "cible/Meta-Llama-3.1-8B-Instruct-bnb-4bit" : (
        "cible/Meta-Llama-3.1-8B-Instruct",
        "meta-llama/Meta-Llama-3.1-8B-Instruct",
    ),
    "cible/Meta-Llama-3.1-70B-bnb-4bit" : (
        "meta-llama/Meta-Llama-3.1-70B",
    ),
    "cible/Meta-Llama-3.1-405B-bnb-4bit" : (
        "meta-llama/Meta-Llama-3.1-405B",
    ),
    "cible/Meta-Llama-3.1-405B-Instruct-bnb-4bit" : (
        "meta-llama/Meta-Llama-3.1-405B-Instruct",
    ),
    "cible/Meta-Llama-3.1-70B-Instruct-bnb-4bit" : (
        "meta-llama/Meta-Llama-3.1-70B-Instruct",
    ),
    "cible/Mistral-Large-Instruct-2407-bnb-4bit" : (
        "mistralai/Mistral-Large-Instruct-2407",
    ),
    "cible/gemma-2-2b-bnb-4bit" : (
        "cible/gemma-2-2b",
        "google/gemma-2-2b",
    ),
    "cible/gemma-2-2b-it-bnb-4bit" : (
        "cible/gemma-2-2b-it",
        "google/gemma-2-2b-it",
    ),
}

INT_TO_FLOAT_MAPPER = {}
FLOAT_TO_INT_MAPPER = {}

for key, values in __INT_TO_FLOAT_MAPPER.items():
    INT_TO_FLOAT_MAPPER[key] = values[0]

    for value in values:
        FLOAT_TO_INT_MAPPER[value] = key
    pass

    # Get lowercased
    lowered_key = key.lower()
    INT_TO_FLOAT_MAPPER[lowered_key] = values[0].lower()

    for value in values:
        FLOAT_TO_INT_MAPPER[value.lower()] = lowered_key
    pass
pass
