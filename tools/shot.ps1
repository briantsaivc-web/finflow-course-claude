# shot.ps1  usage: powershell -ExecutionPolicy Bypass -File shot.ps1 -Name <file> [-Mode full|fg|window] [-Title <keyword>]
param(
  [Parameter(Mandatory=$true)][string]$Name,
  [string]$Mode = "full",
  [string]$Title = ""
)
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;
using System.Text;
public class W {
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc cb, IntPtr lp);
  [DllImport("user32.dll")] public static extern int GetWindowText(IntPtr h, StringBuilder s, int n);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("dwmapi.dll")] public static extern int DwmGetWindowAttribute(IntPtr h, int a, out RECT r, int s);
  public delegate bool EnumProc(IntPtr h, IntPtr lp);
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; }
  public static IntPtr FindByTitle(string key) {
    IntPtr found = IntPtr.Zero;
    EnumWindows((h, lp) => {
      if (!IsWindowVisible(h)) return true;
      var sb = new StringBuilder(512); GetWindowText(h, sb, 512);
      if (sb.ToString().IndexOf(key, StringComparison.OrdinalIgnoreCase) >= 0) { found = h; return false; }
      return true;
    }, IntPtr.Zero);
    return found;
  }
  public static RECT Rect(IntPtr h) {
    RECT r; if (DwmGetWindowAttribute(h, 9, out r, Marshal.SizeOf(typeof(RECT))) != 0) GetWindowRect(h, out r); return r;
  }
}
"@
[W]::SetProcessDPIAware() | Out-Null
$scr = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$x=$scr.X; $y=$scr.Y; $w=$scr.Width; $h=$scr.Height
if ($Mode -eq "fg" -or $Mode -eq "window") {
  if ($Mode -eq "fg") { $hw = [W]::GetForegroundWindow() } else { $hw = [W]::FindByTitle($Title) }
  if ($hw -eq [IntPtr]::Zero) { throw "window not found: $Title" }
  $r = [W]::Rect($hw)
  $x=$r.L; $y=$r.T; $w=$r.R-$r.L; $h=$r.B-$r.T
}
$bmp = New-Object System.Drawing.Bitmap($w, $h)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.CopyFromScreen($x, $y, 0, 0, $bmp.Size)
$dir = Join-Path $env:USERPROFILE "Pictures\finflow-course-shots\raw"
New-Item -ItemType Directory -Force -Path $dir | Out-Null
$p = Join-Path $dir ($Name + ".png")
$bmp.Save($p)
Write-Output ("saved " + $p + " " + $w + "x" + $h + " screen=" + $scr.Width + "x" + $scr.Height)
