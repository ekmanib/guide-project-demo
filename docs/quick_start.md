# Quick Start

## Step1: Setup

After clone this repo to local, setup:

```shell
make setup
```

There are some connivent shortcut commands in the [makefile](https://makefiletutorial.com/) so that you can run some common commands in your terminal quickly. For example, try:

```shell
make test
```

That will test the codes in your repo. All the tests should pass.

## Step2: Write your test

Then, run the following command lines:

```shell
poetry run python src/doc_me.py
```

It should automatically calculate the areas of a circle and a rectangle.

The first challenge is to write document for this script. Simultaneously, you should write your own test function for it in `tests/write_test.py`. You should use `pytest` framework to do so. When you finished, run `make test` again, it should still pass if everything goes well.

Switch `check_mode` from `False` to `True` on the config file `config/test.yaml`. Then, test your repo again. If the docs you wrote earlier was robust and good enough, more tests should be passed.

If not all the tests passed, you can check the report by run:

```shell
make report
```

It will redirect you to a web page with a [allure-pytest report](https://docs.qameta.io/allure/). You can check what happened in log like this:

![Check where is wrong in the log](https://songshgeo-picgo-1302043007.cos.ap-beijing.myqcloud.com/uPic/CleanShot%202023-09-21%20at%2021.00.17@2x.png)

## Step3: format codes

If you've passed all the test in the previous step, we will dive into deeper. Again, in the `config/test.yaml`, set `check_all` to `True` and run the codebase again. You will find most of tests cannot pass. Modify your codes format, can you pass the tests?

## Even more

Finally, write some demo documents in `docs` folder, run `mkdocs serve` and inspect your documents under `API` section. Are you satisfied with your docs? Feel free to modify your docs for a better interpretation for your users.

Install `pre-commit` and try to use it before push your code to the remote branch (the two commands in the same, and the first one is more general):

```shell
poetry run pre-commit install
make install-pre-commit
```

Then, before commit your changes of codebase, try to run `poetry run pre-commit`, your codebase can be uploaded only if everything goes well.
