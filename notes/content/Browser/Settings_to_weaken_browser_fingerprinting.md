## Settings to weaken browser fingerprinting

The most revealing fingerprinting features are fonts, "user-agent", and plug-ins. Values for these features can be examined at http://browserspy.dk.

To weaken fingerprinting with these features in Firefox, go to `about:config`.

 1. **Plug-ins**. Plug-ins are more serious than fonts, since fonts are usually revealed by the Flash plug-in; suppressing Flash's default behavior cloaks fonts.

   2. `plugins.enumerable_names`: set value to empty string to cloak all plug-in names; set to `*` to reveal all. Common names that may be revealed are `QuickTime,Shockwave,Silverlight`.
   2. `plugins.click_to_play`: set to `true` to prevent Java and Flash from running automatically; this may prevent fonts from being enumerated.
   2. It is also possible to go to `about:addons` and set the `Shockwave Flash` add-on to "ask to activate".
 
 1. **User-agent** strings.
 
   2. There are currently (20141227) add-ons called [User Agent Overrider](https://addons.mozilla.org/en-US/firefox/addon/user-agent-overrider/) and [User Agent Switcher](https://addons.mozilla.org/en-US/firefox/addon/user-agent-switcher/) for assisting the changing of this value.
 
[end]
