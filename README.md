# Programming assignment 1.6 BotHeat.py

You can preview this assignment on https://mude.citg.tudelft.nl/workbook-2025/assignments/PA1.6/README.html. This preview doesn't include a preview of the `.py` files. You can obtain your personal repository for submission on: https://classroom.github.com/a/TTP4Saia

Before you can start this assignment, read the theory pages in the book chapter [Large language models](https://mude.citg.tudelft.nl/2025/book/programming/week_1_6.html):
- [Effective prompting](https://mude.citg.tudelft.nl/book/2025/_git/github.com_TeachBooks_learn-programming/mude-2025/book/llms/effective-prompting.html)
- [Generating code exercise](https://mude.citg.tudelft.nl/book/2025/_git/github.com_TeachBooks_learn-programming/mude-2025/book/llms/generating-code.html)
- [Debugging errors exercise](https://mude.citg.tudelft.nl/book/2025/_git/github.com_TeachBooks_learn-programming/mude-2025/book/llms/debugging-errors.html)
- [The importance of human-in-the-loop](https://mude.citg.tudelft.nl/book/2025/_git/github.com_TeachBooks_learn-programming/mude-2025/book/llms/human-in-the-loop.html)

In this assignment you'll make exercises on:

1. [Python scripts in VS Code](./1_py_files.md)
2. [Activate GitHub Copilot in VS Code](./2_activate_github_copilot.md)
3. [Programming a Thermostat with AI](./3_programming_a_thermostat_with_ai.ipynb)

Beware, the third assignment can be a bit of a challenge. But try to co-program with GitHub Copilot! There's no need to complete it fully, as long as you fulfill the criteria below.

You pass this PA if you:
- You've created a new python script called `my_first_script.py` which returns correct results
- You've completed the thermostat scripts. Note that this doesn't require you to write all code yourself, you can use GitHub Copilot to help you. Furthermore, part of it is already implemented, and not all missing parts of the package are required to be completed
  - The onoff controller works correctly:
    - Turns heating on when the temperature drops below the lower deadband limit.
    - Turns heating off when the temperature rises above the upper deadband limit.
    - Maintains the current state when the temperature is within the deadband.
    - Activates a safety cutoff and turns heating off if the temperature reaches the safety high limit.
  - The predictive on/off controller passes the following tests:
    - It turns heating off early if the predicted temperature will exceed the upper deadband limit, even if the current temperature is below the threshold.
    - It turns heating on when the temperature is falling and the predicted value will drop below the lower deadband limit.

> By Tom van Woudenberg and Stanislaw Ostyk-Narbutt, Delft University of Technology. CC BY 4.0, more info [on the Credits page of Workbook](https://mude.citg.tudelft.nl/workbook-2025/credits.html).
