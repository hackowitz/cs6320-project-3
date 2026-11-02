# CS 6320 Project 3: Camera Projection Matrix and Fundamental Matrix Estimation

## Setup

0. Unzip the project and enter its folder: `unzip proj3_6320.zip && cd proj3_6320`
1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) if you do not have conda.
2. Create the environment, substituting your OS (`linux`, `mac`, or `win`):
   `conda env create -f proj3_env_<OS>.yml`
   On Windows run this from the "Anaconda Prompt"; on macOS and Linux any terminal works.
3. Activate it: `conda activate proj3`
4. Install the project package from this folder: `pip install -e .`
5. Start Jupyter from this folder with `jupyter notebook`, then open
   `proj3_code/proj3.ipynb`. The notebook uses paths relative to `proj3_code/`
   (`../data/`, `../results/`), so leave it where it is.
6. Answer every question in the notebook, including the AI-use disclosure at the end.
   The notebook is the report: run all cells before you submit so the figures and printed
   output are saved in the file.
7. Build your submission: `python zip_submission.py --uid <your_uid>`

## Checking your work

Each part of the notebook calls `verify(...)` on the relevant unit tests, which print
`"Correct"` or `"Wrong"` inline. To run the whole suite at once, from this folder:

    cd proj3_code && python -m pytest unit_tests -q

`"Wrong"` means an assertion failed. Call the test function directly (for example
`test_projection()`) to see the message, which names what mismatched.

## Photographs you need to take

Parts 1.6-1.8 and 2.2 need your own images. Take them early.

- **Parts 1.6-1.8:** two photos of a rigid object you can measure with a ruler (a thick
  textbook works well), against a plain contrasting background, from two clearly
  different viewpoints.
- **Part 2.2:** two photos of a textured scene with content at a range of depths, taken
  from two positions separated by a real translation - not a rotation in place, and not
  a zoom. Question 2.3.1 asks you why.

Save them in `data/` and point the notebook at them. Example images ship with the project
(`new_book_img1.jpg`, `new_book_img2.jpg`, `my_image_0_new.jpg`, `my_image_1_new.jpg`) so
every cell runs before you have your own, and so you can see the kind of framing that
works. **You are graded on your own images**, so replace the filenames.

## Notes

- `results/` already exists; the notebook writes your measurements and output images there.
- Use relative paths only. Absolute paths will break on the grader's machine.
- Please do not install extra packages: the graders run this exact environment.
