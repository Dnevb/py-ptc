
plymouth = """
[Plymouth Theme]
Name={0}
Description={1}
ModuleName=script

[script]
ImageDir=/usr/share/plymouth/themes/{0}/animation
ScriptFile=/usr/share/plymouth/themes/{0}/{0}.script
"""

script = """
Window.SetBackgroundTopColor(0.0,0.00,0.0);
Window.SetBackgroundBottomColor(0.0,0.00,0.0);

for(i=0; i < {0}; i++)
  img[i] = Image("{1}-"+i+".png");

isprite= Sprite();
isprite.SetX(Window.GetWidth() / 2 - img.getWidth() / 2);
isprite.SetY(Window.GetHeight() / 2 - img.getHeight() / 2);

progress = 0;

fun refresh_callback(){{
  isprite.SetImage(img[Math.Int(progress / 3) % {0}]);
  progress++;
}}

Plymouth.SetRefreshFunction(refresh_callback)
"""