# Step by step to create a python library.

## Prequisite modules:
1. unittest - to check if all good with the package
2. twine - to check/publish your package
3. wheel - to build your package

## Create the following folder structure:

    abc <main folder>
        xyz <package folder>
            __init__.py
            module.py
        tests <testing package>
            __init__.py
            module_tests.py
        main.py <Some examples with import>
        README.md <Guidance template>
        requirements.txt <if any dependencies required for the package>
        setup.py <trigger the library builder>

## Steps:
1. Once all the folder structure is ready, create the virutal environment in python.
2. check your module is running fine using unittest library. Command: `python -m unittest -v tests/multiplication_tests.py`.
3. Install wheel and twine, if not installed using pip command.
4. Add the .gitignore file to exclude irrevelant files for the package and git repository. This can be generated using gitignore.io website.
5. Create a setup.py files by following the file present in the folder.
6. create a build using wheel library and setup.py file. Command : `python setup.py sdist bdist_wheel`
7. Check the build using twine. Command : `twine check dist/*`
8. Before pushing to test pypi. Make sure you have an account and api is set. Username will be __token__ and password will be api key.
9. Once everything is passed, push it to test pypi to check if good to push on pypi.
<br>Command : `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
<br>Twine will ask for username and password. Kindly provide this as mentioned in step 8.
<br>Once all went correct, you can see the library on test pypi package manager.
<br>This can be installed using pypi from anywhere.

10. For Pypi package manager, repeat steps from 8 and 9.