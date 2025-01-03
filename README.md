<p align="center">  
    <img src="https://tools.etdon.com/placeholder-image/generate?width=830&height=207&background-color=393E41,1E2019,D3D0CB,1E2019&text=detect-compression&text-color=FFFFFF" width=830 height=207>    
</p>

## 🔰 Introduction

The `detect-compression` project is a simple and easy to use script for detecting the compression algorithm used for the provided input.
It is powered by magic value analysis that allows the script to detect over 20 (including sub-types) popular compression algorithms.
While relying purely on magic value analysis of the header for compression algorithm detection is generally speaking not fully dependable
the system is processing in a most-to-least confident order and will provide meaningful results in common scenarios.

## 🚀 Getting Started

> [!IMPORTANT]
> Requirements:
> - Python 3

To download the script click on the green `Code` button and select `Download ZIP`. After unpacking the downloaded `.zip` archive you
will be able to run the script by executing the following command:
```
python detect_compression.py <input>
```
The `input` parameter can either be a path to a file or a hex value. If a file path is provided the script will read the first 8 bytes of it and treat it as the input magic value for analysis.

## 🫴 Contributing
The contribution guidelines are a part of the `shared-guidelines` repository and can be found here: [Contributing][contributing]

## 📄 License
The `detect-compression` project is licensed under the [Apache 2.0 License][license].
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

[contributing]: https://github.com/etdon/shared-guidelines/blob/main/CONTRIBUTING.md
[license]: https://github.com/etdon/detect-compression/blob/master/LICENSE
