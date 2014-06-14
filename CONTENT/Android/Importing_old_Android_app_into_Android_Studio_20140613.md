## Importing old Android app into Android Studio 20140613

 1. Opened Android SDK Manager and updated SDK to API 16 (the one in use when the code was originally written and working).

 1. Imported old code into Android Studio. Build => Make Project. Error:

   > Gradle: 
   > FAILURE: Could not determine which tasks to execute.
   >
   > * What went wrong:
   > Task 'assemble' not found in root project 'MyProject'.
   > 
   > * Try:
   > Run gradle tasks to get a list of available tasks.

    On [http://tools.android.com/knownissues](http://tools.android.com/knownissues) found: "Task 'assemble' not found", advising: 

   > The real problem is that previous version of Android Studio misconfigured the IDEA file (e.g. MyProject.iml) -- it added an extra "`<component name="FacetManager">`" XML element that shouldn't be present. In the case above, the solution is to edit "MyProject.iml" and to remove the "`<component name="FacetManager">`" part

   Removed `<component ... </component>`.

 1. New error:

   > Error:The SDK Build Tools revision (19.0.3) is too low for project ':app'. Minimum required is 19.1.0
   > 
Downloaded `Android SDK tools Rev. 22.6.3` and `Android SDK Build-tools Rev. 19.1`. New error:
   >
   > Error:The SDK Build Tools revision (19.0.3) is too low for project ':app'. Minimum required is 19.1.0

   Now Android SDK Manager cannot be found. Page http://developer.android.com/tools/help/sdk-manager.html says:

   > From Android Studio, select Tools > Android > SDK Manager.

   There is no `Android` in the tools menu. Instead

        cd /Applications/Android\ Studio.app/sdk/tools
        ./android sdk

   Android SDK Manager runs. Delete `Android SDK Build-tools Rev. 17` and `Android SDK Build-tools Rev. 19.0.3`,  and install `Android SDK Platform-tools, revision 19.0.2`. Leave `API 16` installed.

 1. New error:

   > Exception in thread "main" java.lang.NoClassDefFoundError: junit/textui/ResultPrinter

   Following discussion at http://stackoverflow.com/a/19517160/621762: Removed JUnit configuration: Run => Edit Configurations; clicked on JUnit/Suozi and then clicked `-` button to delete.

 1. New error:

   > Error: No Android facet found in the module.

    Following discussion at http://stackoverflow.com/a/17627677/621762: File => Project Structure. 

   2. Project: Chose project SDK of API 19.
   2. Facets: Pressed `+` and chose `Android-Gradle`. 
   2. But error persists. Note that much earlier we removed a `FacetManager` component. Don't know what to do next.

[end]
