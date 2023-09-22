# Improving your python project formats

Fork this repo, try to add some documents, to fix the format problems, and test your progress!

## Quick Start

After clone this repo to local, setup the project and have a quick test with the simplest `makefile` shortcuts:

```shell
make setup
make test
```

The first challenge is to write document for this script. After do so, switch `check_mode` from `False` to `True` on the config file `config/test.yaml`. Then, test your repo again. If the docs you wrote earlier was robust and good enough, more tests should be passed.

If not all the tests passed, you can check the report by run:

```shell
make report
```

It will redirect you to a web page with a [allure-pytest report](https://docs.qameta.io/allure/). You can check what happened in log like this:

![Check where is wrong in the log](https://songshgeo-picgo-1302043007.cos.ap-beijing.myqcloud.com/uPic/CleanShot%202023-09-21%20at%2021.00.17@2x.png)

Based on the report, keep improving your code formats until all tests are passed.

There are even more tests, please check the document for the [full get-start guide](https://songshgeo.github.io/guide-project-demo).
