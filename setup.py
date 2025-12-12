import setuptools

setuptools.setup(
        name="sub-module",
        version="0.0.1",
        python_requires=">=3.6",
        packages=["anglosaxon"],
        install_requires=['torch','torch.nn','torch','torch.nn.functional','numpy','torch.utils.data']
        )
