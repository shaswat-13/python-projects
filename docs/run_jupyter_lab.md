# Running JupyterLab in the python_small_programs Directory

This guide outlines the steps to launch and use JupyterLab specifically within your `python_small_programs` directory, utilizing the virtual environment you've set up.

## Step 1: Activate Your `.venv` Environment

1.  Open your Terminal application.
2.  Navigate to your `python_small_programs` directory using the `cd` command:
    ```bash
    cd Documents/python_small_programs
    ```
3.  Activate the `.venv` virtual environment:
    ```bash
    source .venv/bin/activate
    ```
    Your terminal prompt should now be prefixed with `(.venv)`, indicating the environment is active.

## Step 2: Install JupyterLab (If Not Already Installed in `.venv`)

1.  Ensure your `.venv` environment is active (prompt starts with `(.venv)`).
2.  Use `pip` to install JupyterLab within this environment:
    ```bash
    pip install jupyterlab
    ```
    If JupyterLab is already installed, this command will either upgrade it or indicate that the requirements are already satisfied.

## Step 3: Launch JupyterLab

1.  With your `.venv` environment still active in the terminal.
2.  Run the command to launch JupyterLab:
    ```bash
    jupyter lab
    ```
    This will start the JupyterLab server and automatically open the JupyterLab interface in your default web browser. The file browser in JupyterLab should show the contents of your `python_small_programs` directory.

## Step 4: Open Your `.ipynb` File

1.  In the JupyterLab interface in your web browser, use the file browser on the left sidebar to locate and double-click on your `.ipynb` file within the `python_small_programs` directory. The notebook will open in the main area.

## Step 5: Select the Correct Kernel

Ensure your notebook is using the `python_small_programs_kernel` associated with your `.venv`.

1.  At the top of the JupyterLab interface, you'll see an indicator of the current kernel (e.g., "Python 3").
2.  Go to the **Kernel** menu at the top of the JupyterLab window.
3.  Select **"Change Kernel..."**
4.  In the dialog box, choose **`python_small_programs_kernel`** from the list and click **"Select"**.

## Step 6: Run Your Code

You can now execute the cells in your Jupyter Notebook. JupyterLab will use the Python interpreter and libraries installed within your `.venv` environment.

## Step 7: Quitting JupyterLab

1.  **Save Your Work:** Ensure all your notebooks and files are saved in JupyterLab.
2.  **Close the Browser Tab:** Close the web browser tab where JupyterLab is running.
3.  **Shut Down the Server in the Terminal:**
    * Go to the terminal window where you launched JupyterLab.
    * Press `Ctrl + C`.
    * You might be prompted to confirm. If so, type `y` and press Enter.
4.  **(Optional) Deactivate the Virtual Environment:** Once the JupyterLab server is shut down, you can deactivate your `.venv` by typing `deactivate` in the terminal and pressing Enter. Your terminal prompt will return to normal.