import setuptools

setuptools.setup(
    name="poly",
    version="0.0.0",
    packages=["poly"],
    package_data={"": ["template.template"]},
    include_package_data=True,
    python_requires=">=3.10",
)
