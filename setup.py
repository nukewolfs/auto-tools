from setuptools import setup, find_packages

setup(
    name='autotools-nukewolfs',
    version='1.0.0',
    description='办公自动化工具箱 - 批量处理文件Excel',
    author='nukewolfs',
    author_email='nukewolf@qq.com',
    url='https://github.com/nukewolfs/auto-tools',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'openpyxl>=3.0.0',
    ],
    entry_points={
        'console_scripts': [
            'autotools=autotools:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.7',
)
