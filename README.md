# A.B.R.A. v.01
Arnold Beauty Re-build App (A.B.R.A.) is an application that creates a node graph by shuffling all the necessary AOVs which contain lighting data (e.g. Diffuse, Specular, Transmission) of the selected light group for a beauty rebuild workflow in Nuke using Arnold. This application will allow Nuke compositors that work with Arnold to save time with only a couple of clicks and inputs. Check out this [short demo for the app.] (https://vimeo.com/roo3d/abra)

## Installation
Here’s how to install and use the Nuke Survival Toolkit:

1. Download the .zip folder from the github website.

2. Copy or move the abra Folder either in your User/.nuke/ folder for personal use, or for use in a pipeline or to share with multiple artists, place the folder in any shared and accessible network folder.

3. Open your init.py file in your /.nuke/ folder into any text editor (or create a new init.py in your User/.nuke/ directory if one doesn’t already exist).

4. Copy the following code into your init.py file:

    ```
   nuke.pluginAddPath('Your/ABRA/FolderPath/Here')
   ```

6. Copy the filepath location of where you placed your ABRA folder. Replace the Your/ABRA/FolderPath/Here text with your ABRA filepath location, making sure to keep quotation marks around the filepath

7. Save your init.py file.

8. Open the menu.py file thats inisde the ABRA folder using the text editor of your preference.

9. Inside you will find the code that creates the menu and toolbar for the application. Each menu item comes shipped with an specific icon that are included in the ABRA/icons folder that you downloaded.

10. Copy the filepath location of where you placed your ABRA folder, like so:

     ```
    C:/Downloads/abra
12. Paste the copied text with your ABRA filepath location next to the existing text that goes after icon = , making sure to keep quotation marks around the filepath:\

     ```
    BEFORE:
    icon= '/icons/roo_lgt.png'

    AFTER:
    icon= 'C:/Downloads/abra/icons/roo_lgt.png'
14. Repeat this step for all the existing icons.

15. Save your menu.py file under your User/.nuke/ directory and restart your Nuke session.

16. That’s it! Congrats, you will now see a white icon in your nuke toolbar and can start using the application!
    



## Usage
So far the A.B.R.A. script has the following commands available:

+ Create AOV node graph
+ Create Backdrop
+ Help

### **Creating the AOV node graph**

1. Select the Read node

2. Select **Create AOV node graph** from the menu or toolbar.

3. Write the name of your desired light group in the input window.

Afterwards the full node grpah should be created. The script won't work properly if you don't select a read node first.

### **Creating a Backdrop**

1. Select desiered nodes.

2. Select **Create backdrop** from the menu or toolbar.

3. Write the name of the backdrop in the input window. There is some predefined text in the window for formatting purposes (center & bold).

### **Help Command**
If selected from the menu you will be redirected to my Github page.

## Author
[Rodrigo Ortega](https://www.linkedin.com/in/roo3dcg/) - Lighting & Compositing Artist

[Demo reel](https://vimeo.com/roo3d/lgtdemoreel)
