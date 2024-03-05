from setuptools import setup, find_packages

setup(
    name="proxyapp_google3",
    version="1.0",
    packages=find_packages(),
    package_data={"": ["*.yml", "*.yaml"]},
    include_package_data=True,
    zip_safe=False,
)
