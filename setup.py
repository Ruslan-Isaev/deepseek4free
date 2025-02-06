from setuptools import setup, find_packages
setup(
    name='DeepSeek4Free',
    version='1.0',
    packages=find_packages(),
    install_requires=['curl-cffi==0.8.1b9', 'wasmtime', 'numpy', 'drissionpage', 'setuptools'],
    url='https://github.com/Ruslan-Isaev/deepseek4free',
    description='Deepseek V3 and R1 private API, deep thinking, search, full requests. pow challenge reversed. deepseek api.',
    package_data={
        '': ['wasm/*.wasm'],
    },
    include_package_data=True,
)
