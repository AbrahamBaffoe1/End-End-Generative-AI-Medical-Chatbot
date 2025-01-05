#  this will turn our our project into a package and can be foundn using pip list

from setuptools import find_packages, setup

setup(
    name='Medical Chatbot System',
    version='0.0.1',
    packages=find_packages(),
    license='MIT',
    author='Abraham Kwanme Baffoe',
    author_email='official.abraham.baffoe@gmail.com',
    include_package_data=True,
    description='Langchain',
    install_requires=[
        # 'langchain',
        # 'sentence_transformers',
        # 'pypdf',
        # 'pypdf2',
        # 'pinecone',
        # 'langchain-pinecone',
        # 'langchain_community',
        # 'langchain_openai',
        # 'langchain_experimental',
    ],
)
