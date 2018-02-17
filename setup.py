from setuptools import setup


setup(
    name="scaleman-digitalocean-agent",
    version="0.0.1",
    author="smit thakkar",
    author_email="smitthakkar96@gmail.com",
    description=("An agent that sends cpu usage to given scaleman endpoint"),
    packages=['core'],
    license="BSD",
    url="https://github.com/scaleman/scaleman-agent",
    install_requires=['pandas', 'requests'],
    include_package_data=True,
    zip_safe=False,
    scripts=[
        'bin/scaleman-agent'
    ]
)
