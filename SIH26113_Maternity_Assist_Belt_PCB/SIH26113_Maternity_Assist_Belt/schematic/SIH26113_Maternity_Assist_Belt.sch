<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.6.2">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="1.27" unitdist="mm" unit="mm" style="lines" multiple="1" display="no" altdistance="0.1" altunitdist="mm" altunit="mm"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="yes" active="yes"/>
<layer number="2" name="Route2" color="1" fill="3" visible="yes" active="yes"/>
<layer number="15" name="Route15" color="4" fill="6" visible="yes" active="yes"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="yes" active="yes"/>
<layer number="17" name="Pads" color="2" fill="1" visible="yes" active="yes"/>
<layer number="18" name="Vias" color="2" fill="1" visible="yes" active="yes"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="yes" active="yes"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="yes" active="yes"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="yes" active="yes"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="yes" active="yes"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="yes" active="yes"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="yes" active="yes"/>
<layer number="25" name="tNames" color="7" fill="1" visible="yes" active="yes"/>
<layer number="26" name="bNames" color="7" fill="1" visible="yes" active="yes"/>
<layer number="27" name="tValues" color="7" fill="1" visible="yes" active="yes"/>
<layer number="28" name="bValues" color="7" fill="1" visible="yes" active="yes"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="yes"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="yes"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="yes"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="yes"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="yes"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="yes"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="yes"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="yes"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="yes"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="yes"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="yes" active="yes"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="yes" active="yes"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="yes" active="yes"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="yes" active="yes"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="yes" active="yes"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="yes"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="yes"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="yes"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="yes"/>
<layer number="48" name="Document" color="7" fill="1" visible="yes" active="yes"/>
<layer number="49" name="Reference" color="7" fill="1" visible="yes" active="yes"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="yes" active="yes"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="SIH26113_Maternity_Assist_Belt">
<description>&amp;lt;b&amp;gt;SIH26113 - Maternity Assist Belt&amp;lt;/b&amp;gt;&amp;lt;p&amp;gt;Prototype carrier-board library. Every footprint is derived from the manufacturer's package-outline or recommended land-pattern drawing, or from IPC-7351B Nominal density for generic package families. Pin electrical types are set for real ERC use - nothing is blanket-marked passive.&amp;lt;p&amp;gt;NOT A MEDICAL DEVICE. See documentation/REQUIRES_CONFIRMATION.md.</description>
<packages>
<package name="ESP32-S3-WROOM-1">
<description>Espressif ESP32-S3-WROOM-1 module land pattern. Source: ESP32-S3-WROOM-1/1U datasheet v1.8 Fig.11-1 + Fig.10-1. 40 lands 1.5x0.9 mm, 1.27 mm pitch, 17.5 mm row spacing, pin 1 at 7.49 mm from the antenna edge. 6 mm antenna keepout at +Y.</description>
<smd name="1" x="-8.75" y="5.26" dx="1.5" dy="0.9" layer="1"/>
<smd name="2" x="-8.75" y="3.99" dx="1.5" dy="0.9" layer="1"/>
<smd name="3" x="-8.75" y="2.72" dx="1.5" dy="0.9" layer="1"/>
<smd name="4" x="-8.75" y="1.45" dx="1.5" dy="0.9" layer="1"/>
<smd name="5" x="-8.75" y="0.18" dx="1.5" dy="0.9" layer="1"/>
<smd name="6" x="-8.75" y="-1.09" dx="1.5" dy="0.9" layer="1"/>
<smd name="7" x="-8.75" y="-2.36" dx="1.5" dy="0.9" layer="1"/>
<smd name="8" x="-8.75" y="-3.63" dx="1.5" dy="0.9" layer="1"/>
<smd name="9" x="-8.75" y="-4.9" dx="1.5" dy="0.9" layer="1"/>
<smd name="10" x="-8.75" y="-6.17" dx="1.5" dy="0.9" layer="1"/>
<smd name="11" x="-8.75" y="-7.44" dx="1.5" dy="0.9" layer="1"/>
<smd name="12" x="-8.75" y="-8.71" dx="1.5" dy="0.9" layer="1"/>
<smd name="13" x="-8.75" y="-9.98" dx="1.5" dy="0.9" layer="1"/>
<smd name="14" x="-8.75" y="-11.25" dx="1.5" dy="0.9" layer="1"/>
<smd name="15" x="-6.985" y="-12.5" dx="0.9" dy="1.5" layer="1"/>
<smd name="16" x="-5.715" y="-12.5" dx="0.9" dy="1.5" layer="1"/>
<smd name="17" x="-4.445" y="-12.5" dx="0.9" dy="1.5" layer="1"/>
<smd name="18" x="-3.175" y="-12.5" dx="0.9" dy="1.5" layer="1"/>
<smd name="19" x="-1.905" y="-12.5" dx="0.9" dy="1.5" layer="1"/>
<smd name="20" x="-0.635" y="-12.5" dx="0.9" dy="1.5" layer="1"/>
<smd name="21" x="0.635" y="-12.5" dx="0.9" dy="1.5" layer="1"/>
<smd name="22" x="1.905" y="-12.5" dx="0.9" dy="1.5" layer="1"/>
<smd name="23" x="3.175" y="-12.5" dx="0.9" dy="1.5" layer="1"/>
<smd name="24" x="4.445" y="-12.5" dx="0.9" dy="1.5" layer="1"/>
<smd name="25" x="5.715" y="-12.5" dx="0.9" dy="1.5" layer="1"/>
<smd name="26" x="6.985" y="-12.5" dx="0.9" dy="1.5" layer="1"/>
<smd name="27" x="8.75" y="-11.25" dx="1.5" dy="0.9" layer="1"/>
<smd name="28" x="8.75" y="-9.98" dx="1.5" dy="0.9" layer="1"/>
<smd name="29" x="8.75" y="-8.71" dx="1.5" dy="0.9" layer="1"/>
<smd name="30" x="8.75" y="-7.44" dx="1.5" dy="0.9" layer="1"/>
<smd name="31" x="8.75" y="-6.17" dx="1.5" dy="0.9" layer="1"/>
<smd name="32" x="8.75" y="-4.9" dx="1.5" dy="0.9" layer="1"/>
<smd name="33" x="8.75" y="-3.63" dx="1.5" dy="0.9" layer="1"/>
<smd name="34" x="8.75" y="-2.36" dx="1.5" dy="0.9" layer="1"/>
<smd name="35" x="8.75" y="-1.09" dx="1.5" dy="0.9" layer="1"/>
<smd name="36" x="8.75" y="0.18" dx="1.5" dy="0.9" layer="1"/>
<smd name="37" x="8.75" y="1.45" dx="1.5" dy="0.9" layer="1"/>
<smd name="38" x="8.75" y="2.72" dx="1.5" dy="0.9" layer="1"/>
<smd name="39" x="8.75" y="3.99" dx="1.5" dy="0.9" layer="1"/>
<smd name="40" x="8.75" y="5.26" dx="1.5" dy="0.9" layer="1"/>
<smd name="41" x="-1.25" y="-2.5" dx="3.4" dy="3.4" layer="1" thermals="no"/>
<wire x1="-9" y1="12.75" x2="9" y2="12.75" width="0.15" layer="21"/>
<wire x1="-9" y1="12.75" x2="-9" y2="6.01" width="0.15" layer="21"/>
<wire x1="9" y1="12.75" x2="9" y2="6.01" width="0.15" layer="21"/>
<wire x1="-9" y1="6.75" x2="9" y2="6.75" width="0.15" layer="21"/>
<text x="-8" y="8.55" size="1" layer="21" ratio="10">ANTENNA - KEEP CLEAR</text>
<circle x="-10.1" y="5.26" radius="0.25" width="0.2" layer="21"/>
<rectangle x1="-9" y1="-12.75" x2="9" y2="12.75" layer="51"/>
<rectangle x1="-9" y1="6.75" x2="9" y2="12.75" layer="41"/>
<rectangle x1="-9" y1="6.75" x2="9" y2="12.75" layer="42"/>
<rectangle x1="-9" y1="6.75" x2="9" y2="12.75" layer="43"/>
<rectangle x1="-9" y1="6.75" x2="9" y2="12.75" layer="39"/>
<text x="-9" y="-14.35" size="1.1" layer="25" ratio="10">&gt;NAME</text>
<text x="-9" y="-15.95" size="1.1" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="LFCSP-20-4X4-P050">
<description>20-lead LFCSP_WQ 4x4 mm, 0.5 mm pitch, 2.50 mm SQ exposed pad (ADI CP-20-10 / JEDEC MO-220-WGGD). Body+terminal dims verified from the AD8232 Rev.A outline drawing; lands are IPC-7351B Nominal (0.80 x 0.28 mm at 1.75 mm from centre).</description>
<smd name="1" x="-1.75" y="1" dx="0.8" dy="0.28" layer="1"/>
<smd name="2" x="-1.75" y="0.5" dx="0.8" dy="0.28" layer="1"/>
<smd name="3" x="-1.75" y="0" dx="0.8" dy="0.28" layer="1"/>
<smd name="4" x="-1.75" y="-0.5" dx="0.8" dy="0.28" layer="1"/>
<smd name="5" x="-1.75" y="-1" dx="0.8" dy="0.28" layer="1"/>
<smd name="6" x="-1" y="-1.75" dx="0.28" dy="0.8" layer="1"/>
<smd name="7" x="-0.5" y="-1.75" dx="0.28" dy="0.8" layer="1"/>
<smd name="8" x="0" y="-1.75" dx="0.28" dy="0.8" layer="1"/>
<smd name="9" x="0.5" y="-1.75" dx="0.28" dy="0.8" layer="1"/>
<smd name="10" x="1" y="-1.75" dx="0.28" dy="0.8" layer="1"/>
<smd name="11" x="1.75" y="-1" dx="0.8" dy="0.28" layer="1"/>
<smd name="12" x="1.75" y="-0.5" dx="0.8" dy="0.28" layer="1"/>
<smd name="13" x="1.75" y="0" dx="0.8" dy="0.28" layer="1"/>
<smd name="14" x="1.75" y="0.5" dx="0.8" dy="0.28" layer="1"/>
<smd name="15" x="1.75" y="1" dx="0.8" dy="0.28" layer="1"/>
<smd name="16" x="1" y="1.75" dx="0.28" dy="0.8" layer="1"/>
<smd name="17" x="0.5" y="1.75" dx="0.28" dy="0.8" layer="1"/>
<smd name="18" x="0" y="1.75" dx="0.28" dy="0.8" layer="1"/>
<smd name="19" x="-0.5" y="1.75" dx="0.28" dy="0.8" layer="1"/>
<smd name="20" x="-1" y="1.75" dx="0.28" dy="0.8" layer="1"/>
<smd name="EP" x="0" y="0" dx="2.5" dy="2.5" layer="1" thermals="no"/>
<wire x1="-2.15" y1="1.5" x2="-2.15" y2="2.15" width="0.12" layer="21"/>
<wire x1="-2.15" y1="2.15" x2="-1.5" y2="2.15" width="0.12" layer="21"/>
<wire x1="2.15" y1="1.5" x2="2.15" y2="2.15" width="0.12" layer="21"/>
<wire x1="2.15" y1="2.15" x2="1.5" y2="2.15" width="0.12" layer="21"/>
<wire x1="-2.15" y1="-1.5" x2="-2.15" y2="-2.15" width="0.12" layer="21"/>
<wire x1="-2.15" y1="-2.15" x2="-1.5" y2="-2.15" width="0.12" layer="21"/>
<wire x1="2.15" y1="-1.5" x2="2.15" y2="-2.15" width="0.12" layer="21"/>
<wire x1="2.15" y1="-2.15" x2="1.5" y2="-2.15" width="0.12" layer="21"/>
<circle x="-2.55" y="1.9" radius="0.18" width="0.18" layer="21"/>
<rectangle x1="-2" y1="-2" x2="2" y2="2" layer="51"/>
<text x="-2" y="2.6" size="0.9" layer="25" ratio="10">&gt;NAME</text>
<text x="-2" y="-3.5" size="0.9" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="WSON-6-DRV0006B">
<description>TI DRV0006B 6-pin WSON 2.0x2.0 mm, 0.65 mm pitch, thermal pad 1.0x1.6 mm. Lands 0.45x0.30 mm at 1.95 mm row spacing, taken directly from TI's EXAMPLE BOARD LAYOUT (TMP117 SNOSD82D p.41). Pad 7 = exposed thermal pad.</description>
<smd name="1" x="-0.975" y="0.65" dx="0.45" dy="0.3" layer="1"/>
<smd name="2" x="-0.975" y="0" dx="0.45" dy="0.3" layer="1"/>
<smd name="3" x="-0.975" y="-0.65" dx="0.45" dy="0.3" layer="1"/>
<smd name="4" x="0.975" y="-0.65" dx="0.45" dy="0.3" layer="1"/>
<smd name="5" x="0.975" y="0" dx="0.45" dy="0.3" layer="1"/>
<smd name="6" x="0.975" y="0.65" dx="0.45" dy="0.3" layer="1"/>
<smd name="7" x="0" y="0" dx="1" dy="1.6" layer="1" thermals="no"/>
<wire x1="-1.1" y1="1.1" x2="-0.6" y2="1.1" width="0.1" layer="21"/>
<wire x1="1.1" y1="1.1" x2="0.6" y2="1.1" width="0.1" layer="21"/>
<wire x1="-1.1" y1="-1.1" x2="-0.6" y2="-1.1" width="0.1" layer="21"/>
<wire x1="1.1" y1="-1.1" x2="0.6" y2="-1.1" width="0.1" layer="21"/>
<circle x="-1.45" y="0.9" radius="0.15" width="0.15" layer="21"/>
<rectangle x1="-1" y1="-1" x2="1" y2="1" layer="51"/>
<text x="-1" y="1.5" size="0.8" layer="25" ratio="10">&gt;NAME</text>
<text x="-1" y="-2.3" size="0.8" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="LGA-14L-2.5X3.0">
<description>ST LGA-14L 2.5x3.0x0.86 mm. Body/pad geometry from LSM6DSOX DS12814 Rev.4 Fig.28 (14 pads 0.475x0.25 mm, 0.5 mm pitch, 1.5/1.0 mm row spans). Lands enlarged to 0.50x0.28 mm per IPC-7351B Nominal. Drawn in board top view (package bottom view mirrored).</description>
<smd name="1" x="1.025" y="0.75" dx="0.45" dy="0.25" layer="1"/>
<smd name="2" x="1.025" y="0.25" dx="0.45" dy="0.25" layer="1"/>
<smd name="3" x="1.025" y="-0.25" dx="0.45" dy="0.25" layer="1"/>
<smd name="4" x="1.025" y="-0.75" dx="0.45" dy="0.25" layer="1"/>
<smd name="5" x="0.5" y="-1.275" dx="0.25" dy="0.45" layer="1"/>
<smd name="6" x="0" y="-1.275" dx="0.25" dy="0.45" layer="1"/>
<smd name="7" x="-0.5" y="-1.275" dx="0.25" dy="0.45" layer="1"/>
<smd name="8" x="-1.025" y="-0.75" dx="0.45" dy="0.25" layer="1"/>
<smd name="9" x="-1.025" y="-0.25" dx="0.45" dy="0.25" layer="1"/>
<smd name="10" x="-1.025" y="0.25" dx="0.45" dy="0.25" layer="1"/>
<smd name="11" x="-1.025" y="0.75" dx="0.45" dy="0.25" layer="1"/>
<smd name="12" x="-0.5" y="1.275" dx="0.25" dy="0.45" layer="1"/>
<smd name="13" x="0" y="1.275" dx="0.25" dy="0.45" layer="1"/>
<smd name="14" x="0.5" y="1.275" dx="0.25" dy="0.45" layer="1"/>
<wire x1="1.37" y1="1.62" x2="0.95" y2="1.62" width="0.1" layer="21"/>
<wire x1="1.37" y1="1.62" x2="1.37" y2="1.2" width="0.1" layer="21"/>
<wire x1="-1.37" y1="-1.62" x2="-0.95" y2="-1.62" width="0.1" layer="21"/>
<wire x1="-1.37" y1="-1.62" x2="-1.37" y2="-1.2" width="0.1" layer="21"/>
<circle x="1.7" y="1.4" radius="0.15" width="0.15" layer="21"/>
<rectangle x1="-1.25" y1="-1.5" x2="1.25" y2="1.5" layer="51"/>
<text x="-1.25" y="2.05" size="0.8" layer="25" ratio="10">&gt;NAME</text>
<text x="-1.25" y="-2.85" size="0.8" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="SOIC-8-N">
<description>SOIC-8 narrow (150 mil body). Body 4.90 x 3.90 mm, lead span 6.00 mm, 1.27 mm pitch. Lands 1.55 x 0.60 mm at 5.40 mm span (IPC-7351B SOIC127P600X175-8N Nominal).</description>
<smd name="1" x="-2.7" y="1.905" dx="1.55" dy="0.6" layer="1"/>
<smd name="2" x="-2.7" y="0.635" dx="1.55" dy="0.6" layer="1"/>
<smd name="3" x="-2.7" y="-0.635" dx="1.55" dy="0.6" layer="1"/>
<smd name="4" x="-2.7" y="-1.905" dx="1.55" dy="0.6" layer="1"/>
<smd name="5" x="2.7" y="-1.905" dx="1.55" dy="0.6" layer="1"/>
<smd name="6" x="2.7" y="-0.635" dx="1.55" dy="0.6" layer="1"/>
<smd name="7" x="2.7" y="0.635" dx="1.55" dy="0.6" layer="1"/>
<smd name="8" x="2.7" y="1.905" dx="1.55" dy="0.6" layer="1"/>
<wire x1="-1.95" y1="2.45" x2="1.95" y2="2.45" width="0.12" layer="21"/>
<wire x1="-1.95" y1="-2.45" x2="1.95" y2="-2.45" width="0.12" layer="21"/>
<wire x1="-1.95" y1="2.45" x2="-1.95" y2="2.05" width="0.12" layer="21"/>
<wire x1="-1.95" y1="-2.45" x2="-1.95" y2="-2.05" width="0.12" layer="21"/>
<wire x1="1.95" y1="2.45" x2="1.95" y2="2.05" width="0.12" layer="21"/>
<wire x1="1.95" y1="-2.45" x2="1.95" y2="-2.05" width="0.12" layer="21"/>
<circle x="-3.825" y="1.905" radius="0.15" width="0.15" layer="21"/>
<rectangle x1="-1.95" y1="-2.45" x2="1.95" y2="2.45" layer="51"/>
<text x="-1.95" y="3.05" size="0.9" layer="25" ratio="10">&gt;NAME</text>
<text x="-1.95" y="-3.95" size="0.9" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="SOP-16-N">
<description>SOP-16L narrow. Body 9.90 x 3.90 mm, lead span 6.00 mm, 1.27 mm pitch (HX711 datasheet Package Dimensions). Lands 1.55 x 0.60 mm at 5.40 mm span (IPC-7351B SOIC127P600X175-16N Nominal).</description>
<smd name="1" x="-2.7" y="4.445" dx="1.55" dy="0.6" layer="1"/>
<smd name="2" x="-2.7" y="3.175" dx="1.55" dy="0.6" layer="1"/>
<smd name="3" x="-2.7" y="1.905" dx="1.55" dy="0.6" layer="1"/>
<smd name="4" x="-2.7" y="0.635" dx="1.55" dy="0.6" layer="1"/>
<smd name="5" x="-2.7" y="-0.635" dx="1.55" dy="0.6" layer="1"/>
<smd name="6" x="-2.7" y="-1.905" dx="1.55" dy="0.6" layer="1"/>
<smd name="7" x="-2.7" y="-3.175" dx="1.55" dy="0.6" layer="1"/>
<smd name="8" x="-2.7" y="-4.445" dx="1.55" dy="0.6" layer="1"/>
<smd name="9" x="2.7" y="-4.445" dx="1.55" dy="0.6" layer="1"/>
<smd name="10" x="2.7" y="-3.175" dx="1.55" dy="0.6" layer="1"/>
<smd name="11" x="2.7" y="-1.905" dx="1.55" dy="0.6" layer="1"/>
<smd name="12" x="2.7" y="-0.635" dx="1.55" dy="0.6" layer="1"/>
<smd name="13" x="2.7" y="0.635" dx="1.55" dy="0.6" layer="1"/>
<smd name="14" x="2.7" y="1.905" dx="1.55" dy="0.6" layer="1"/>
<smd name="15" x="2.7" y="3.175" dx="1.55" dy="0.6" layer="1"/>
<smd name="16" x="2.7" y="4.445" dx="1.55" dy="0.6" layer="1"/>
<wire x1="-1.95" y1="4.95" x2="1.95" y2="4.95" width="0.12" layer="21"/>
<wire x1="-1.95" y1="-4.95" x2="1.95" y2="-4.95" width="0.12" layer="21"/>
<wire x1="-1.95" y1="4.95" x2="-1.95" y2="4.55" width="0.12" layer="21"/>
<wire x1="-1.95" y1="-4.95" x2="-1.95" y2="-4.55" width="0.12" layer="21"/>
<wire x1="1.95" y1="4.95" x2="1.95" y2="4.55" width="0.12" layer="21"/>
<wire x1="1.95" y1="-4.95" x2="1.95" y2="-4.55" width="0.12" layer="21"/>
<circle x="-3.825" y="4.445" radius="0.15" width="0.15" layer="21"/>
<rectangle x1="-1.95" y1="-4.95" x2="1.95" y2="4.95" layer="51"/>
<text x="-1.95" y="5.55" size="0.9" layer="25" ratio="10">&gt;NAME</text>
<text x="-1.95" y="-6.45" size="0.9" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="SOT-23-5">
<description>SOT-23-5 (Diodes 'SOT25', JEDEC TO-178). 0.95 mm pitch, lands 1.10 x 0.60 mm at 2.60 mm row span (IPC-7351B SOT95P280X145-5N Nominal). Pin order per AP2112 datasheet: 1 VIN, 2 GND, 3 EN, 4 NC, 5 VOUT.</description>
<smd name="1" x="-0.95" y="-1.3" dx="0.6" dy="1.1" layer="1"/>
<smd name="2" x="0" y="-1.3" dx="0.6" dy="1.1" layer="1"/>
<smd name="3" x="0.95" y="-1.3" dx="0.6" dy="1.1" layer="1"/>
<smd name="4" x="0.95" y="1.3" dx="0.6" dy="1.1" layer="1"/>
<smd name="5" x="-0.95" y="1.3" dx="0.6" dy="1.1" layer="1"/>
<wire x1="-1.45" y1="-1.5" x2="1.45" y2="-1.5" width="0.12" layer="21"/>
<wire x1="-1.45" y1="1.5" x2="1.45" y2="1.5" width="0.12" layer="21"/>
<wire x1="-1.45" y1="-1.5" x2="-1.45" y2="1.5" width="0.12" layer="21"/>
<wire x1="1.45" y1="-1.5" x2="1.45" y2="1.5" width="0.12" layer="21"/>
<circle x="-1.8" y="-1.3" radius="0.15" width="0.15" layer="21"/>
<rectangle x1="-1.45" y1="-1.5" x2="1.45" y2="1.5" layer="51"/>
<text x="-1.45" y="2.1" size="0.8" layer="25" ratio="10">&gt;NAME</text>
<text x="-1.45" y="-2.9" size="0.8" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="SOT-23-3">
<description>SOT-23-3. Lands 1.00 x 0.60 mm, 2.30 mm row span, 1.90 mm pad 1-2 spacing (IPC-7351B SOT95P237X112-3N Nominal). Standard N-MOSFET assignment: 1 = Gate, 2 = Source, 3 = Drain.</description>
<smd name="1" x="-0.95" y="-1.15" dx="0.6" dy="1" layer="1"/>
<smd name="2" x="0.95" y="-1.15" dx="0.6" dy="1" layer="1"/>
<smd name="3" x="0" y="1.15" dx="0.6" dy="1" layer="1"/>
<wire x1="-1.45" y1="-1.5" x2="1.45" y2="-1.5" width="0.12" layer="21"/>
<wire x1="-1.45" y1="1.5" x2="1.45" y2="1.5" width="0.12" layer="21"/>
<wire x1="-1.45" y1="-1.5" x2="-1.45" y2="1.5" width="0.12" layer="21"/>
<wire x1="1.45" y1="-1.5" x2="1.45" y2="1.5" width="0.12" layer="21"/>
<circle x="-1.8" y="-1.15" radius="0.15" width="0.15" layer="21"/>
<rectangle x1="-1.45" y1="-1.5" x2="1.45" y2="1.5" layer="51"/>
<text x="-1.45" y="2.1" size="0.8" layer="25" ratio="10">&gt;NAME</text>
<text x="-1.45" y="-2.9" size="0.8" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="R0805">
<description>0805 (2012 metric) chip resistor. IPC-7351B RESC2012X65N Nominal: lands 1.15 x 1.40 mm, 0.75 mm inner gap.</description>
<smd name="1" x="-0.95" y="0" dx="1.15" dy="1.4" layer="1"/>
<smd name="2" x="0.95" y="0" dx="1.15" dy="1.4" layer="1"/>
<wire x1="-1.775" y1="-0.8" x2="-1.775" y2="0.8" width="0.12" layer="21"/>
<wire x1="1.775" y1="-0.8" x2="1.775" y2="0.8" width="0.12" layer="21"/>
<rectangle x1="-1" y1="-0.625" x2="1" y2="0.625" layer="51"/>
<wire x1="-2.125" y1="-1.15" x2="2.125" y2="-1.15" width="0.05" layer="39"/>
<wire x1="2.125" y1="-1.15" x2="2.125" y2="1.15" width="0.05" layer="39"/>
<wire x1="2.125" y1="1.15" x2="-2.125" y2="1.15" width="0.05" layer="39"/>
<wire x1="-2.125" y1="1.15" x2="-2.125" y2="-1.15" width="0.05" layer="39"/>
<text x="-1.775" y="1.3" size="0.8" layer="25" ratio="10">&gt;NAME</text>
<text x="-1.775" y="-2.1" size="0.8" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="C0805">
<description>0805 (2012 metric) chip capacitor. IPC-7351B CAPC2012X135N Nominal: lands 1.15 x 1.40 mm, 0.75 mm inner gap.</description>
<smd name="1" x="-0.95" y="0" dx="1.15" dy="1.4" layer="1"/>
<smd name="2" x="0.95" y="0" dx="1.15" dy="1.4" layer="1"/>
<wire x1="-1.775" y1="-0.8" x2="-1.775" y2="0.8" width="0.12" layer="21"/>
<wire x1="1.775" y1="-0.8" x2="1.775" y2="0.8" width="0.12" layer="21"/>
<rectangle x1="-1" y1="-0.625" x2="1" y2="0.625" layer="51"/>
<wire x1="-2.125" y1="-1.15" x2="2.125" y2="-1.15" width="0.05" layer="39"/>
<wire x1="2.125" y1="-1.15" x2="2.125" y2="1.15" width="0.05" layer="39"/>
<wire x1="2.125" y1="1.15" x2="-2.125" y2="1.15" width="0.05" layer="39"/>
<wire x1="-2.125" y1="1.15" x2="-2.125" y2="-1.15" width="0.05" layer="39"/>
<text x="-1.775" y="1.3" size="0.8" layer="25" ratio="10">&gt;NAME</text>
<text x="-1.775" y="-2.1" size="0.8" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="LED0805">
<description>0805 chip LED, polarised. Pad 1 = cathode (marked by the extra silkscreen bar).</description>
<smd name="1" x="-0.95" y="0" dx="1.15" dy="1.4" layer="1"/>
<smd name="2" x="0.95" y="0" dx="1.15" dy="1.4" layer="1"/>
<wire x1="-1.775" y1="-0.8" x2="-1.775" y2="0.8" width="0.12" layer="21"/>
<wire x1="1.775" y1="-0.8" x2="1.775" y2="0.8" width="0.12" layer="21"/>
<wire x1="-2.025" y1="-0.8" x2="-2.025" y2="0.8" width="0.2" layer="21"/>
<rectangle x1="-1" y1="-0.625" x2="1" y2="0.625" layer="51"/>
<wire x1="-2.125" y1="-1.15" x2="2.125" y2="-1.15" width="0.05" layer="39"/>
<wire x1="2.125" y1="-1.15" x2="2.125" y2="1.15" width="0.05" layer="39"/>
<wire x1="2.125" y1="1.15" x2="-2.125" y2="1.15" width="0.05" layer="39"/>
<wire x1="-2.125" y1="1.15" x2="-2.125" y2="-1.15" width="0.05" layer="39"/>
<text x="-1.775" y="1.3" size="0.8" layer="25" ratio="10">&gt;NAME</text>
<text x="-1.775" y="-2.1" size="0.8" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="SOD-123">
<description>SOD-123 diode. Body 2.65 x 1.60 mm. Lands 1.20 x 1.10 mm at 1.30 mm inner gap (IPC-7351B DIOM2616X110N Nominal). Pad 1 = cathode (band).</description>
<smd name="1" x="-1.25" y="0" dx="1.2" dy="1.1" layer="1"/>
<smd name="2" x="1.25" y="0" dx="1.2" dy="1.1" layer="1"/>
<wire x1="-2.1" y1="-0.9" x2="-2.1" y2="0.9" width="0.12" layer="21"/>
<wire x1="2.1" y1="-0.9" x2="2.1" y2="0.9" width="0.12" layer="21"/>
<wire x1="-2.35" y1="-0.9" x2="-2.35" y2="0.9" width="0.2" layer="21"/>
<rectangle x1="-1.325" y1="-0.8" x2="1.325" y2="0.8" layer="51"/>
<wire x1="-2.45" y1="-1.25" x2="2.45" y2="-1.25" width="0.05" layer="39"/>
<wire x1="2.45" y1="-1.25" x2="2.45" y2="1.25" width="0.05" layer="39"/>
<wire x1="2.45" y1="1.25" x2="-2.45" y2="1.25" width="0.05" layer="39"/>
<wire x1="-2.45" y1="1.25" x2="-2.45" y2="-1.25" width="0.05" layer="39"/>
<text x="-2.1" y="1.4" size="0.8" layer="25" ratio="10">&gt;NAME</text>
<text x="-2.1" y="-2.2" size="0.8" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="JST-PH-2">
<description>JST PH series 2-circuit top-entry through-hole header (S2B-PH-K-S). 2.00 mm pitch, PCB hole 0.7 +0.1 mm per the JST ePH PC-board-layout figure; drill specified 0.8 mm for FR-4. Pad 1 is square.</description>
<pad name="1" x="-1" y="0" drill="0.8" diameter="1.5" shape="square"/>
<pad name="2" x="1" y="0" drill="0.8" diameter="1.5"/>
<wire x1="-2.95" y1="-1.7" x2="2.95" y2="-1.7" width="0.12" layer="21"/>
<wire x1="2.95" y1="-1.7" x2="2.95" y2="2.8" width="0.12" layer="21"/>
<wire x1="2.95" y1="2.8" x2="-2.95" y2="2.8" width="0.12" layer="21"/>
<wire x1="-2.95" y1="2.8" x2="-2.95" y2="-1.7" width="0.12" layer="21"/>
<wire x1="-2.95" y1="-1.7" x2="-2.15" y2="-1.7" width="0.35" layer="21"/>
<rectangle x1="-2.95" y1="-1.7" x2="2.95" y2="2.8" layer="51"/>
<text x="-2.95" y="3.1" size="0.9" layer="25" ratio="10">&gt;NAME</text>
<text x="-2.95" y="-3.3" size="0.9" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="JST-PH-4">
<description>JST PH series 4-circuit top-entry through-hole header (S4B-PH-K-S). 2.00 mm pitch, PCB hole 0.7 +0.1 mm per the JST ePH PC-board-layout figure; drill specified 0.8 mm for FR-4. Pad 1 is square.</description>
<pad name="1" x="-3" y="0" drill="0.8" diameter="1.5" shape="square"/>
<pad name="2" x="-1" y="0" drill="0.8" diameter="1.5"/>
<pad name="3" x="1" y="0" drill="0.8" diameter="1.5"/>
<pad name="4" x="3" y="0" drill="0.8" diameter="1.5"/>
<wire x1="-4.95" y1="-1.7" x2="4.95" y2="-1.7" width="0.12" layer="21"/>
<wire x1="4.95" y1="-1.7" x2="4.95" y2="2.8" width="0.12" layer="21"/>
<wire x1="4.95" y1="2.8" x2="-4.95" y2="2.8" width="0.12" layer="21"/>
<wire x1="-4.95" y1="2.8" x2="-4.95" y2="-1.7" width="0.12" layer="21"/>
<wire x1="-4.95" y1="-1.7" x2="-4.15" y2="-1.7" width="0.35" layer="21"/>
<rectangle x1="-4.95" y1="-1.7" x2="4.95" y2="2.8" layer="51"/>
<text x="-4.95" y="3.1" size="0.9" layer="25" ratio="10">&gt;NAME</text>
<text x="-4.95" y="-3.3" size="0.9" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="HDR-1X2">
<description>1x2 2.54 mm through-hole pin header. Drill 1.0 mm / pad 1.8 mm suits the 0.64 mm square posts used by all common 2.54 mm headers. Pad 1 is square.</description>
<pad name="1" x="-1.27" y="0" drill="1" diameter="1.8" shape="square"/>
<pad name="2" x="1.27" y="0" drill="1" diameter="1.8"/>
<wire x1="-2.54" y1="-1.27" x2="2.54" y2="-1.27" width="0.12" layer="21"/>
<wire x1="2.54" y1="-1.27" x2="2.54" y2="1.27" width="0.12" layer="21"/>
<wire x1="2.54" y1="1.27" x2="-2.54" y2="1.27" width="0.12" layer="21"/>
<wire x1="-2.54" y1="1.27" x2="-2.54" y2="-1.27" width="0.12" layer="21"/>
<wire x1="-2.54" y1="0.67" x2="-1.94" y2="1.27" width="0.2" layer="21"/>
<text x="-2.54" y="1.67" size="0.9" layer="25" ratio="10">&gt;NAME</text>
<text x="-2.54" y="-2.77" size="0.9" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="HDR-1X3">
<description>1x3 2.54 mm through-hole pin header. Drill 1.0 mm / pad 1.8 mm suits the 0.64 mm square posts used by all common 2.54 mm headers. Pad 1 is square.</description>
<pad name="1" x="-2.54" y="0" drill="1" diameter="1.8" shape="square"/>
<pad name="2" x="0" y="0" drill="1" diameter="1.8"/>
<pad name="3" x="2.54" y="0" drill="1" diameter="1.8"/>
<wire x1="-3.81" y1="-1.27" x2="3.81" y2="-1.27" width="0.12" layer="21"/>
<wire x1="3.81" y1="-1.27" x2="3.81" y2="1.27" width="0.12" layer="21"/>
<wire x1="3.81" y1="1.27" x2="-3.81" y2="1.27" width="0.12" layer="21"/>
<wire x1="-3.81" y1="1.27" x2="-3.81" y2="-1.27" width="0.12" layer="21"/>
<wire x1="-3.81" y1="0.67" x2="-3.21" y2="1.27" width="0.2" layer="21"/>
<text x="-3.81" y="1.67" size="0.9" layer="25" ratio="10">&gt;NAME</text>
<text x="-3.81" y="-2.77" size="0.9" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="HDR-1X4">
<description>1x4 2.54 mm through-hole pin header. Drill 1.0 mm / pad 1.8 mm suits the 0.64 mm square posts used by all common 2.54 mm headers. Pad 1 is square.</description>
<pad name="1" x="-3.81" y="0" drill="1" diameter="1.8" shape="square"/>
<pad name="2" x="-1.27" y="0" drill="1" diameter="1.8"/>
<pad name="3" x="1.27" y="0" drill="1" diameter="1.8"/>
<pad name="4" x="3.81" y="0" drill="1" diameter="1.8"/>
<wire x1="-5.08" y1="-1.27" x2="5.08" y2="-1.27" width="0.12" layer="21"/>
<wire x1="5.08" y1="-1.27" x2="5.08" y2="1.27" width="0.12" layer="21"/>
<wire x1="5.08" y1="1.27" x2="-5.08" y2="1.27" width="0.12" layer="21"/>
<wire x1="-5.08" y1="1.27" x2="-5.08" y2="-1.27" width="0.12" layer="21"/>
<wire x1="-5.08" y1="0.67" x2="-4.48" y2="1.27" width="0.2" layer="21"/>
<text x="-5.08" y="1.67" size="0.9" layer="25" ratio="10">&gt;NAME</text>
<text x="-5.08" y="-2.77" size="0.9" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="HDR-1X5">
<description>1x5 2.54 mm through-hole pin header. Drill 1.0 mm / pad 1.8 mm suits the 0.64 mm square posts used by all common 2.54 mm headers. Pad 1 is square.</description>
<pad name="1" x="-5.08" y="0" drill="1" diameter="1.8" shape="square"/>
<pad name="2" x="-2.54" y="0" drill="1" diameter="1.8"/>
<pad name="3" x="0" y="0" drill="1" diameter="1.8"/>
<pad name="4" x="2.54" y="0" drill="1" diameter="1.8"/>
<pad name="5" x="5.08" y="0" drill="1" diameter="1.8"/>
<wire x1="-6.35" y1="-1.27" x2="6.35" y2="-1.27" width="0.12" layer="21"/>
<wire x1="6.35" y1="-1.27" x2="6.35" y2="1.27" width="0.12" layer="21"/>
<wire x1="6.35" y1="1.27" x2="-6.35" y2="1.27" width="0.12" layer="21"/>
<wire x1="-6.35" y1="1.27" x2="-6.35" y2="-1.27" width="0.12" layer="21"/>
<wire x1="-6.35" y1="0.67" x2="-5.75" y2="1.27" width="0.2" layer="21"/>
<text x="-6.35" y="1.67" size="0.9" layer="25" ratio="10">&gt;NAME</text>
<text x="-6.35" y="-2.77" size="0.9" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="HDR-1X6">
<description>1x6 2.54 mm through-hole pin header. Drill 1.0 mm / pad 1.8 mm suits the 0.64 mm square posts used by all common 2.54 mm headers. Pad 1 is square.</description>
<pad name="1" x="-6.35" y="0" drill="1" diameter="1.8" shape="square"/>
<pad name="2" x="-3.81" y="0" drill="1" diameter="1.8"/>
<pad name="3" x="-1.27" y="0" drill="1" diameter="1.8"/>
<pad name="4" x="1.27" y="0" drill="1" diameter="1.8"/>
<pad name="5" x="3.81" y="0" drill="1" diameter="1.8"/>
<pad name="6" x="6.35" y="0" drill="1" diameter="1.8"/>
<wire x1="-7.62" y1="-1.27" x2="7.62" y2="-1.27" width="0.12" layer="21"/>
<wire x1="7.62" y1="-1.27" x2="7.62" y2="1.27" width="0.12" layer="21"/>
<wire x1="7.62" y1="1.27" x2="-7.62" y2="1.27" width="0.12" layer="21"/>
<wire x1="-7.62" y1="1.27" x2="-7.62" y2="-1.27" width="0.12" layer="21"/>
<wire x1="-7.62" y1="0.67" x2="-7.02" y2="1.27" width="0.2" layer="21"/>
<text x="-7.62" y="1.67" size="0.9" layer="25" ratio="10">&gt;NAME</text>
<text x="-7.62" y="-2.77" size="0.9" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="HDR-1X8">
<description>1x8 2.54 mm through-hole pin header. Drill 1.0 mm / pad 1.8 mm suits the 0.64 mm square posts used by all common 2.54 mm headers. Pad 1 is square.</description>
<pad name="1" x="-8.89" y="0" drill="1" diameter="1.8" shape="square"/>
<pad name="2" x="-6.35" y="0" drill="1" diameter="1.8"/>
<pad name="3" x="-3.81" y="0" drill="1" diameter="1.8"/>
<pad name="4" x="-1.27" y="0" drill="1" diameter="1.8"/>
<pad name="5" x="1.27" y="0" drill="1" diameter="1.8"/>
<pad name="6" x="3.81" y="0" drill="1" diameter="1.8"/>
<pad name="7" x="6.35" y="0" drill="1" diameter="1.8"/>
<pad name="8" x="8.89" y="0" drill="1" diameter="1.8"/>
<wire x1="-10.16" y1="-1.27" x2="10.16" y2="-1.27" width="0.12" layer="21"/>
<wire x1="10.16" y1="-1.27" x2="10.16" y2="1.27" width="0.12" layer="21"/>
<wire x1="10.16" y1="1.27" x2="-10.16" y2="1.27" width="0.12" layer="21"/>
<wire x1="-10.16" y1="1.27" x2="-10.16" y2="-1.27" width="0.12" layer="21"/>
<wire x1="-10.16" y1="0.67" x2="-9.56" y2="1.27" width="0.2" layer="21"/>
<text x="-10.16" y="1.67" size="0.9" layer="25" ratio="10">&gt;NAME</text>
<text x="-10.16" y="-2.77" size="0.9" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="TACT-6X6-THT">
<description>6.0 x 6.0 mm through-hole tactile switch, 4 leads on a 6.5 x 4.5 mm grid (TL1105 / B3F-10xx family). Leads 1-2 common, 3-4 common. Drill 1.0 mm. De-facto standard geometry -- confirm against the chosen vendor part before fabrication.</description>
<pad name="1" x="-3.25" y="2.25" drill="1" diameter="1.6" shape="square"/>
<pad name="2" x="-3.25" y="-2.25" drill="1" diameter="1.6"/>
<pad name="3" x="3.25" y="2.25" drill="1" diameter="1.6"/>
<pad name="4" x="3.25" y="-2.25" drill="1" diameter="1.6"/>
<wire x1="-3" y1="-3" x2="3" y2="-3" width="0.12" layer="21"/>
<wire x1="3" y1="-3" x2="3" y2="3" width="0.12" layer="21"/>
<wire x1="3" y1="3" x2="-3" y2="3" width="0.12" layer="21"/>
<wire x1="-3" y1="3" x2="-3" y2="-3" width="0.12" layer="21"/>
<circle x="0" y="0" radius="1.75" width="0.12" layer="21"/>
<rectangle x1="-3" y1="-3" x2="3" y2="3" layer="51"/>
<text x="-3" y="3.4" size="0.9" layer="25" ratio="10">&gt;NAME</text>
<text x="-3" y="-4.6" size="0.9" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="TESTPOINT-1.5">
<description>1.5 mm round SMD test-point land (probe / flying-lead solder point).</description>
<smd name="TP" x="0" y="0" dx="1.5" dy="1.5" layer="1" roundness="100"/>
<circle x="0" y="0" radius="1.1" width="0.1" layer="21"/>
<text x="0" y="1.5" size="0.8" layer="25" ratio="10" align="bottom-center">&gt;NAME</text>
</package>
<package name="MOUNT-M2">
<description>M2 mounting hole. 2.2 mm drill for an M2 screw, 4.4 mm annular copper land (plated, tied to GND) and a 4.6 mm keepout ring.</description>
<pad name="1" x="0" y="0" drill="2.2" diameter="4.4"/>
<circle x="0" y="0" radius="2.3" width="0.15" layer="21"/>
<circle x="0" y="0" radius="2.3" width="0.05" layer="39"/>
<circle x="0" y="0" radius="2.3" width="0.05" layer="41"/>
<circle x="0" y="0" radius="2.3" width="0.05" layer="42"/>
</package>
</packages>
<symbols>
<symbol name="ESP32-S3-WROOM-1">
<description>Espressif ESP32-S3-WROOM-1 Wi-Fi/BLE module</description>
<wire x1="-16.51" y1="-27.94" x2="16.51" y2="-27.94" width="0.254" layer="94"/>
<wire x1="16.51" y1="-27.94" x2="16.51" y2="27.94" width="0.254" layer="94"/>
<wire x1="16.51" y1="27.94" x2="-16.51" y2="27.94" width="0.254" layer="94"/>
<wire x1="-16.51" y1="27.94" x2="-16.51" y2="-27.94" width="0.254" layer="94"/>
<text x="-16.51" y="28.94" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-16.51" y="-30.14" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<text x="-15.81" y="24.85" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-15.81" y="22.31" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-15.81" y="19.77" size="0.9" layer="97" ratio="10">IN</text>
<text x="-15.81" y="17.23" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="14.69" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="12.15" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="9.61" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="7.07" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="4.53" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="1.99" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="-0.55" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="-3.09" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="-5.63" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="-8.17" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="-10.71" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="-13.25" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="-15.79" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="-18.33" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="-20.87" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="-23.41" size="0.9" layer="97" ratio="10">I/O</text>
<text x="-15.81" y="-25.95" size="0.9" layer="97" ratio="10">I/O</text>
<text x="15.81" y="24.85" size="0.9" layer="97" ratio="10" align="bottom-right">PWR</text>
<text x="15.81" y="22.31" size="0.9" layer="97" ratio="10" align="bottom-right">PWR</text>
<text x="15.81" y="19.77" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="17.23" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="14.69" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="12.15" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="9.61" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="7.07" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="4.53" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="1.99" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="-0.55" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="-3.09" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="-5.63" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="-8.17" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="-10.71" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="-13.25" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="-15.79" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="-18.33" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="-20.87" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="15.81" y="-23.41" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="-14" y="-30" size="1.2" layer="97" ratio="10">STRAPPING: IO0 IO3 IO45 IO46</text>
<text x="-14" y="-32" size="1.2" layer="97" ratio="10">ADC1 = IO1..IO10 (Wi-Fi safe)</text>
<text x="-14" y="-34" size="1.2" layer="97" ratio="10">ADC2 = IO11..IO20 (UNUSABLE with Wi-Fi)</text>
<text x="-14" y="-36" size="1.2" layer="97" ratio="10">IO35/36/37: N8R2 only (octal-PSRAM parts reserve them)</text>
<pin name="GND@1" x="-21.59" y="25.4" length="middle" direction="pwr"/>
<pin name="3V3" x="-21.59" y="22.86" length="middle" direction="pwr"/>
<pin name="EN" x="-21.59" y="20.32" length="middle" direction="in"/>
<pin name="IO0" x="-21.59" y="17.78" length="middle"/>
<pin name="IO1" x="-21.59" y="15.24" length="middle"/>
<pin name="IO2" x="-21.59" y="12.7" length="middle"/>
<pin name="IO3" x="-21.59" y="10.16" length="middle"/>
<pin name="IO4" x="-21.59" y="7.62" length="middle"/>
<pin name="IO5" x="-21.59" y="5.08" length="middle"/>
<pin name="IO6" x="-21.59" y="2.54" length="middle"/>
<pin name="IO7" x="-21.59" y="0" length="middle"/>
<pin name="IO8" x="-21.59" y="-2.54" length="middle"/>
<pin name="IO9" x="-21.59" y="-5.08" length="middle"/>
<pin name="IO10" x="-21.59" y="-7.62" length="middle"/>
<pin name="IO11" x="-21.59" y="-10.16" length="middle"/>
<pin name="IO12" x="-21.59" y="-12.7" length="middle"/>
<pin name="IO13" x="-21.59" y="-15.24" length="middle"/>
<pin name="IO14" x="-21.59" y="-17.78" length="middle"/>
<pin name="IO15" x="-21.59" y="-20.32" length="middle"/>
<pin name="IO16" x="-21.59" y="-22.86" length="middle"/>
<pin name="IO17" x="-21.59" y="-25.4" length="middle"/>
<pin name="GND@40" x="21.59" y="25.4" length="middle" direction="pwr" rot="R180"/>
<pin name="EPAD" x="21.59" y="22.86" length="middle" direction="pwr" rot="R180"/>
<pin name="IO18" x="21.59" y="20.32" length="middle" rot="R180"/>
<pin name="IO19" x="21.59" y="17.78" length="middle" rot="R180"/>
<pin name="IO20" x="21.59" y="15.24" length="middle" rot="R180"/>
<pin name="IO21" x="21.59" y="12.7" length="middle" rot="R180"/>
<pin name="IO35" x="21.59" y="10.16" length="middle" rot="R180"/>
<pin name="IO36" x="21.59" y="7.62" length="middle" rot="R180"/>
<pin name="IO37" x="21.59" y="5.08" length="middle" rot="R180"/>
<pin name="IO38" x="21.59" y="2.54" length="middle" rot="R180"/>
<pin name="IO39" x="21.59" y="0" length="middle" rot="R180"/>
<pin name="IO40" x="21.59" y="-2.54" length="middle" rot="R180"/>
<pin name="IO41" x="21.59" y="-5.08" length="middle" rot="R180"/>
<pin name="IO42" x="21.59" y="-7.62" length="middle" rot="R180"/>
<pin name="TXD0" x="21.59" y="-10.16" length="middle" rot="R180"/>
<pin name="RXD0" x="21.59" y="-12.7" length="middle" rot="R180"/>
<pin name="IO45" x="21.59" y="-15.24" length="middle" rot="R180"/>
<pin name="IO46" x="21.59" y="-17.78" length="middle" rot="R180"/>
<pin name="IO47" x="21.59" y="-20.32" length="middle" rot="R180"/>
<pin name="IO48" x="21.59" y="-22.86" length="middle" rot="R180"/>
</symbol>
<symbol name="AD8232">
<description>ADI AD8232 single-lead heart-rate monitor analog front end</description>
<wire x1="-15.24" y1="-15.24" x2="15.24" y2="-15.24" width="0.254" layer="94"/>
<wire x1="15.24" y1="-15.24" x2="15.24" y2="15.24" width="0.254" layer="94"/>
<wire x1="15.24" y1="15.24" x2="-15.24" y2="15.24" width="0.254" layer="94"/>
<wire x1="-15.24" y1="15.24" x2="-15.24" y2="-15.24" width="0.254" layer="94"/>
<text x="-15.24" y="16.24" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-15.24" y="-17.44" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<text x="-14.54" y="12.15" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-14.54" y="9.61" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-14.54" y="7.07" size="0.9" layer="97" ratio="10">IN</text>
<text x="-14.54" y="4.53" size="0.9" layer="97" ratio="10">IN</text>
<text x="-14.54" y="1.99" size="0.9" layer="97" ratio="10">IN</text>
<text x="-14.54" y="-0.55" size="0.9" layer="97" ratio="10">OUT</text>
<text x="-14.54" y="-3.09" size="0.9" layer="97" ratio="10">IN</text>
<text x="-14.54" y="-5.63" size="0.9" layer="97" ratio="10">OUT</text>
<text x="-14.54" y="-8.17" size="0.9" layer="97" ratio="10">IN</text>
<text x="-14.54" y="-10.71" size="0.9" layer="97" ratio="10">IN</text>
<text x="-14.54" y="-13.25" size="0.9" layer="97" ratio="10">IN</text>
<text x="14.54" y="12.15" size="0.9" layer="97" ratio="10" align="bottom-right">OUT</text>
<text x="14.54" y="9.61" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="14.54" y="7.07" size="0.9" layer="97" ratio="10" align="bottom-right">OUT</text>
<text x="14.54" y="4.53" size="0.9" layer="97" ratio="10" align="bottom-right">PAS</text>
<text x="14.54" y="1.99" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="14.54" y="-0.55" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="14.54" y="-3.09" size="0.9" layer="97" ratio="10" align="bottom-right">OUT</text>
<text x="14.54" y="-5.63" size="0.9" layer="97" ratio="10" align="bottom-right">OUT</text>
<text x="14.54" y="-8.17" size="0.9" layer="97" ratio="10" align="bottom-right">OUT</text>
<text x="14.54" y="-10.71" size="0.9" layer="97" ratio="10" align="bottom-right">PWR</text>
<text x="-14" y="-17" size="1.2" layer="97" ratio="10">Vs = 2.0 .. 3.5 V ONLY</text>
<pin name="+VS" x="-20.32" y="12.7" length="middle" direction="pwr"/>
<pin name="GND" x="-20.32" y="10.16" length="middle" direction="pwr"/>
<pin name="+IN" x="-20.32" y="7.62" length="middle" direction="in"/>
<pin name="-IN" x="-20.32" y="5.08" length="middle" direction="in"/>
<pin name="RLDFB" x="-20.32" y="2.54" length="middle" direction="in"/>
<pin name="RLD" x="-20.32" y="0" length="middle" direction="out"/>
<pin name="REFIN" x="-20.32" y="-2.54" length="middle" direction="in"/>
<pin name="REFOUT" x="-20.32" y="-5.08" length="middle" direction="out"/>
<pin name="SDN" x="-20.32" y="-7.62" length="middle" direction="in"/>
<pin name="AC/DC" x="-20.32" y="-10.16" length="middle" direction="in"/>
<pin name="FR" x="-20.32" y="-12.7" length="middle" direction="in"/>
<pin name="IAOUT" x="20.32" y="12.7" length="middle" direction="out" rot="R180"/>
<pin name="HPSENSE" x="20.32" y="10.16" length="middle" direction="in" rot="R180"/>
<pin name="HPDRIVE" x="20.32" y="7.62" length="middle" direction="out" rot="R180"/>
<pin name="SW" x="20.32" y="5.08" length="middle" direction="pas" rot="R180"/>
<pin name="OPAMP+" x="20.32" y="2.54" length="middle" direction="in" rot="R180"/>
<pin name="OPAMP-" x="20.32" y="0" length="middle" direction="in" rot="R180"/>
<pin name="OUT" x="20.32" y="-2.54" length="middle" direction="out" rot="R180"/>
<pin name="LOD+" x="20.32" y="-5.08" length="middle" direction="out" rot="R180"/>
<pin name="LOD-" x="20.32" y="-7.62" length="middle" direction="out" rot="R180"/>
<pin name="EP" x="20.32" y="-10.16" length="middle" direction="pwr" rot="R180"/>
</symbol>
<symbol name="TMP117">
<description>TI TMP117 high-accuracy digital temperature sensor</description>
<wire x1="-11.43" y1="-6.35" x2="11.43" y2="-6.35" width="0.254" layer="94"/>
<wire x1="11.43" y1="-6.35" x2="11.43" y2="6.35" width="0.254" layer="94"/>
<wire x1="11.43" y1="6.35" x2="-11.43" y2="6.35" width="0.254" layer="94"/>
<wire x1="-11.43" y1="6.35" x2="-11.43" y2="-6.35" width="0.254" layer="94"/>
<text x="-11.43" y="7.35" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-11.43" y="-8.55" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<text x="-10.73" y="3.26" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-10.73" y="0.72" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-10.73" y="-1.82" size="0.9" layer="97" ratio="10">IN</text>
<text x="10.73" y="3.26" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="10.73" y="0.72" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="10.73" y="-1.82" size="0.9" layer="97" ratio="10" align="bottom-right">OC</text>
<text x="10.73" y="-4.36" size="0.9" layer="97" ratio="10" align="bottom-right">PWR</text>
<pin name="V+" x="-16.51" y="3.81" length="middle" direction="pwr"/>
<pin name="GND" x="-16.51" y="1.27" length="middle" direction="pwr"/>
<pin name="ADD0" x="-16.51" y="-1.27" length="middle" direction="in"/>
<pin name="SDA" x="16.51" y="3.81" length="middle" rot="R180"/>
<pin name="SCL" x="16.51" y="1.27" length="middle" direction="in" rot="R180"/>
<pin name="ALERT" x="16.51" y="-1.27" length="middle" direction="oc" rot="R180"/>
<pin name="TPAD" x="16.51" y="-3.81" length="middle" direction="pwr" rot="R180"/>
</symbol>
<symbol name="LSM6DSOX">
<description>ST LSM6DSOX 6-axis IMU (accelerometer + gyroscope)</description>
<wire x1="-12.7" y1="-11.43" x2="12.7" y2="-11.43" width="0.254" layer="94"/>
<wire x1="12.7" y1="-11.43" x2="12.7" y2="11.43" width="0.254" layer="94"/>
<wire x1="12.7" y1="11.43" x2="-12.7" y2="11.43" width="0.254" layer="94"/>
<wire x1="-12.7" y1="11.43" x2="-12.7" y2="-11.43" width="0.254" layer="94"/>
<text x="-12.7" y="12.43" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-12.7" y="-13.63" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<text x="-12" y="8.34" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-12" y="5.8" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-12" y="3.26" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-12" y="0.72" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-12" y="-1.82" size="0.9" layer="97" ratio="10">IN</text>
<text x="-12" y="-4.36" size="0.9" layer="97" ratio="10">I/O</text>
<text x="12" y="8.34" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="12" y="5.8" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="12" y="3.26" size="0.9" layer="97" ratio="10" align="bottom-right">OUT</text>
<text x="12" y="0.72" size="0.9" layer="97" ratio="10" align="bottom-right">OUT</text>
<text x="12" y="-1.82" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="12" y="-4.36" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="12" y="-6.9" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="12" y="-9.44" size="0.9" layer="97" ratio="10" align="bottom-right">OUT</text>
<text x="-11" y="-15" size="1.2" layer="97" ratio="10">Mode 1: I2C (CS=1, SDx/SCx tied)</text>
<pin name="VDD" x="-17.78" y="8.89" length="middle" direction="pwr"/>
<pin name="VDDIO" x="-17.78" y="6.35" length="middle" direction="pwr"/>
<pin name="GND@6" x="-17.78" y="3.81" length="middle" direction="pwr"/>
<pin name="GND@7" x="-17.78" y="1.27" length="middle" direction="pwr"/>
<pin name="CS" x="-17.78" y="-1.27" length="middle" direction="in"/>
<pin name="SDO/SA0" x="-17.78" y="-3.81" length="middle"/>
<pin name="SDA" x="17.78" y="8.89" length="middle" rot="R180"/>
<pin name="SCL" x="17.78" y="6.35" length="middle" direction="in" rot="R180"/>
<pin name="INT1" x="17.78" y="3.81" length="middle" direction="out" rot="R180"/>
<pin name="INT2" x="17.78" y="1.27" length="middle" direction="out" rot="R180"/>
<pin name="SDx" x="17.78" y="-1.27" length="middle" rot="R180"/>
<pin name="SCx" x="17.78" y="-3.81" length="middle" rot="R180"/>
<pin name="OCS_AUX" x="17.78" y="-6.35" length="middle" direction="in" rot="R180"/>
<pin name="SDO_AUX" x="17.78" y="-8.89" length="middle" direction="out" rot="R180"/>
</symbol>
<symbol name="AS5600">
<description>ams-OSRAM AS5600 12-bit magnetic rotary position sensor</description>
<wire x1="-12.7" y1="-6.35" x2="12.7" y2="-6.35" width="0.254" layer="94"/>
<wire x1="12.7" y1="-6.35" x2="12.7" y2="6.35" width="0.254" layer="94"/>
<wire x1="12.7" y1="6.35" x2="-12.7" y2="6.35" width="0.254" layer="94"/>
<wire x1="-12.7" y1="6.35" x2="-12.7" y2="-6.35" width="0.254" layer="94"/>
<text x="-12.7" y="7.35" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-12.7" y="-8.55" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<text x="-12" y="3.26" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-12" y="0.72" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-12" y="-1.82" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-12" y="-4.36" size="0.9" layer="97" ratio="10">IN</text>
<text x="12" y="3.26" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="12" y="0.72" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="12" y="-1.82" size="0.9" layer="97" ratio="10" align="bottom-right">OUT</text>
<text x="12" y="-4.36" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="-11" y="-9.5" size="1.2" layer="97" ratio="10">I2C address 0x36 (FIXED)</text>
<pin name="VDD5V" x="-17.78" y="3.81" length="middle" direction="pwr"/>
<pin name="VDD3V3" x="-17.78" y="1.27" length="middle" direction="pwr"/>
<pin name="GND" x="-17.78" y="-1.27" length="middle" direction="pwr"/>
<pin name="DIR" x="-17.78" y="-3.81" length="middle" direction="in"/>
<pin name="SDA" x="17.78" y="3.81" length="middle" rot="R180"/>
<pin name="SCL" x="17.78" y="1.27" length="middle" direction="in" rot="R180"/>
<pin name="OUT" x="17.78" y="-1.27" length="middle" direction="out" rot="R180"/>
<pin name="PGO" x="17.78" y="-3.81" length="middle" direction="in" rot="R180"/>
</symbol>
<symbol name="TP4056">
<description>NanJing Top Power TP4056 1A Li-ion linear charger</description>
<wire x1="-12.7" y1="-6.35" x2="12.7" y2="-6.35" width="0.254" layer="94"/>
<wire x1="12.7" y1="-6.35" x2="12.7" y2="6.35" width="0.254" layer="94"/>
<wire x1="12.7" y1="6.35" x2="-12.7" y2="6.35" width="0.254" layer="94"/>
<wire x1="-12.7" y1="6.35" x2="-12.7" y2="-6.35" width="0.254" layer="94"/>
<text x="-12.7" y="7.35" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-12.7" y="-8.55" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<text x="-12" y="3.26" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-12" y="0.72" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-12" y="-1.82" size="0.9" layer="97" ratio="10">IN</text>
<text x="-12" y="-4.36" size="0.9" layer="97" ratio="10">IN</text>
<text x="12" y="3.26" size="0.9" layer="97" ratio="10" align="bottom-right">OUT</text>
<text x="12" y="0.72" size="0.9" layer="97" ratio="10" align="bottom-right">PAS</text>
<text x="12" y="-1.82" size="0.9" layer="97" ratio="10" align="bottom-right">OC</text>
<text x="12" y="-4.36" size="0.9" layer="97" ratio="10" align="bottom-right">OC</text>
<pin name="VCC" x="-17.78" y="3.81" length="middle" direction="pwr"/>
<pin name="GND" x="-17.78" y="1.27" length="middle" direction="pwr"/>
<pin name="CE" x="-17.78" y="-1.27" length="middle" direction="in"/>
<pin name="TEMP" x="-17.78" y="-3.81" length="middle" direction="in"/>
<pin name="BAT" x="17.78" y="3.81" length="middle" direction="out" rot="R180"/>
<pin name="PROG" x="17.78" y="1.27" length="middle" direction="pas" rot="R180"/>
<pin name="CHRG" x="17.78" y="-1.27" length="middle" direction="oc" rot="R180"/>
<pin name="STDBY" x="17.78" y="-3.81" length="middle" direction="oc" rot="R180"/>
</symbol>
<symbol name="AP2112K">
<description>Diodes AP2112K-3.3 600 mA CMOS LDO regulator with enable</description>
<wire x1="-11.43" y1="-5.08" x2="11.43" y2="-5.08" width="0.254" layer="94"/>
<wire x1="11.43" y1="-5.08" x2="11.43" y2="5.08" width="0.254" layer="94"/>
<wire x1="11.43" y1="5.08" x2="-11.43" y2="5.08" width="0.254" layer="94"/>
<wire x1="-11.43" y1="5.08" x2="-11.43" y2="-5.08" width="0.254" layer="94"/>
<text x="-11.43" y="6.08" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-11.43" y="-7.28" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<text x="-10.73" y="1.99" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-10.73" y="-0.55" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-10.73" y="-3.09" size="0.9" layer="97" ratio="10">IN</text>
<text x="10.73" y="1.99" size="0.9" layer="97" ratio="10" align="bottom-right">PWR</text>
<text x="10.73" y="-0.55" size="0.9" layer="97" ratio="10" align="bottom-right">NC</text>
<pin name="VIN" x="-16.51" y="2.54" length="middle" direction="pwr"/>
<pin name="GND" x="-16.51" y="0" length="middle" direction="pwr"/>
<pin name="EN" x="-16.51" y="-2.54" length="middle" direction="in"/>
<pin name="VOUT" x="16.51" y="2.54" length="middle" direction="pwr" rot="R180"/>
<pin name="NC" x="16.51" y="0" length="middle" direction="nc" rot="R180"/>
</symbol>
<symbol name="HX711">
<description>Avia Semiconductor HX711 24-bit bridge/load-cell ADC</description>
<wire x1="-13.97" y1="-12.7" x2="13.97" y2="-12.7" width="0.254" layer="94"/>
<wire x1="13.97" y1="-12.7" x2="13.97" y2="12.7" width="0.254" layer="94"/>
<wire x1="13.97" y1="12.7" x2="-13.97" y2="12.7" width="0.254" layer="94"/>
<wire x1="-13.97" y1="12.7" x2="-13.97" y2="-12.7" width="0.254" layer="94"/>
<text x="-13.97" y="13.7" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-13.97" y="-14.9" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<text x="-13.27" y="9.61" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-13.27" y="7.07" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-13.27" y="4.53" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-13.27" y="1.99" size="0.9" layer="97" ratio="10">PWR</text>
<text x="-13.27" y="-0.55" size="0.9" layer="97" ratio="10">OUT</text>
<text x="-13.27" y="-3.09" size="0.9" layer="97" ratio="10">IN</text>
<text x="-13.27" y="-5.63" size="0.9" layer="97" ratio="10">OUT</text>
<text x="13.27" y="9.61" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="13.27" y="7.07" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="13.27" y="4.53" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="13.27" y="1.99" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="13.27" y="-0.55" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="13.27" y="-3.09" size="0.9" layer="97" ratio="10" align="bottom-right">OUT</text>
<text x="13.27" y="-5.63" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<text x="13.27" y="-8.17" size="0.9" layer="97" ratio="10" align="bottom-right">I/O</text>
<text x="13.27" y="-10.71" size="0.9" layer="97" ratio="10" align="bottom-right">IN</text>
<pin name="VSUP" x="-19.05" y="10.16" length="middle" direction="pwr"/>
<pin name="AVDD" x="-19.05" y="7.62" length="middle" direction="pwr"/>
<pin name="DVDD" x="-19.05" y="5.08" length="middle" direction="pwr"/>
<pin name="AGND" x="-19.05" y="2.54" length="middle" direction="pwr"/>
<pin name="BASE" x="-19.05" y="0" length="middle" direction="out"/>
<pin name="VFB" x="-19.05" y="-2.54" length="middle" direction="in"/>
<pin name="VBG" x="-19.05" y="-5.08" length="middle" direction="out"/>
<pin name="INA+" x="19.05" y="10.16" length="middle" direction="in" rot="R180"/>
<pin name="INA-" x="19.05" y="7.62" length="middle" direction="in" rot="R180"/>
<pin name="INB+" x="19.05" y="5.08" length="middle" direction="in" rot="R180"/>
<pin name="INB-" x="19.05" y="2.54" length="middle" direction="in" rot="R180"/>
<pin name="PD_SCK" x="19.05" y="0" length="middle" direction="in" rot="R180"/>
<pin name="DOUT" x="19.05" y="-2.54" length="middle" direction="out" rot="R180"/>
<pin name="XI" x="19.05" y="-5.08" length="middle" direction="in" rot="R180"/>
<pin name="XO" x="19.05" y="-7.62" length="middle" rot="R180"/>
<pin name="RATE" x="19.05" y="-10.16" length="middle" direction="in" rot="R180"/>
</symbol>
<symbol name="R">
<description>Resistor</description>
<wire x1="-2.54" y1="0" x2="-1.905" y2="0" width="0.1524" layer="94"/>
<rectangle x1="-1.905" y1="-0.762" x2="1.905" y2="0.762" layer="94"/>
<wire x1="1.905" y1="0" x2="2.54" y2="0" width="0.1524" layer="94"/>
<text x="-2.54" y="1.4" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-2.54" y="-3" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<pin name="1" x="-5.08" y="0" length="short" direction="pas"/>
<pin name="2" x="5.08" y="0" length="short" direction="pas" rot="R180"/>
</symbol>
<symbol name="C">
<description>Capacitor (non-polarised)</description>
<wire x1="-1.27" y1="0.508" x2="1.27" y2="0.508" width="0.254" layer="94"/>
<wire x1="-1.27" y1="-0.508" x2="1.27" y2="-0.508" width="0.254" layer="94"/>
<wire x1="0" y1="0.508" x2="0" y2="2.54" width="0.1524" layer="94"/>
<wire x1="0" y1="-0.508" x2="0" y2="-2.54" width="0.1524" layer="94"/>
<text x="1.9" y="0.9" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="1.9" y="-2.6" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<pin name="1" x="0" y="5.08" length="short" direction="pas" rot="R270"/>
<pin name="2" x="0" y="-5.08" length="short" direction="pas" rot="R90"/>
</symbol>
<symbol name="LED">
<description>Light-emitting diode</description>
<wire x1="-1.27" y1="1.27" x2="-1.27" y2="-1.27" width="0.254" layer="94"/>
<wire x1="-1.27" y1="0" x2="1.27" y2="1.27" width="0.254" layer="94"/>
<wire x1="1.27" y1="1.27" x2="1.27" y2="-1.27" width="0.254" layer="94"/>
<wire x1="1.27" y1="-1.27" x2="-1.27" y2="0" width="0.254" layer="94"/>
<wire x1="1.9" y1="1.6" x2="3.2" y2="2.9" width="0.1524" layer="94"/>
<wire x1="2.4" y1="1.1" x2="3.7" y2="2.4" width="0.1524" layer="94"/>
<text x="-2.54" y="-4.2" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="4" y="-4.2" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<text x="-1.2" y="2" size="0.9" layer="97" ratio="10">K</text>
<text x="0.9" y="2" size="0.9" layer="97" ratio="10">A</text>
<pin name="C" x="-3.81" y="0" length="short" direction="pas"/>
<pin name="A" x="3.81" y="0" length="short" direction="pas" rot="R180"/>
</symbol>
<symbol name="DIODE">
<description>Diode (Schottky / rectifier)</description>
<wire x1="-1.27" y1="1.27" x2="-1.27" y2="-1.27" width="0.254" layer="94"/>
<wire x1="-1.27" y1="0" x2="1.27" y2="1.27" width="0.254" layer="94"/>
<wire x1="1.27" y1="1.27" x2="1.27" y2="-1.27" width="0.254" layer="94"/>
<wire x1="1.27" y1="-1.27" x2="-1.27" y2="0" width="0.254" layer="94"/>
<text x="-2.54" y="2" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-2.54" y="-4" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<text x="-1.2" y="-2.4" size="0.9" layer="97" ratio="10">K</text>
<text x="0.9" y="-2.4" size="0.9" layer="97" ratio="10">A</text>
<pin name="C" x="-3.81" y="0" length="short" direction="pas"/>
<pin name="A" x="3.81" y="0" length="short" direction="pas" rot="R180"/>
</symbol>
<symbol name="NMOS">
<description>N-channel enhancement MOSFET</description>
<wire x1="-2.54" y1="0" x2="-1.27" y2="0" width="0.1524" layer="94"/>
<wire x1="-1.27" y1="2.032" x2="-1.27" y2="-2.032" width="0.254" layer="94"/>
<wire x1="-0.508" y1="2.032" x2="-0.508" y2="1.016" width="0.254" layer="94"/>
<wire x1="-0.508" y1="0.508" x2="-0.508" y2="-0.508" width="0.254" layer="94"/>
<wire x1="-0.508" y1="-1.016" x2="-0.508" y2="-2.032" width="0.254" layer="94"/>
<wire x1="-0.508" y1="1.524" x2="2.54" y2="1.524" width="0.1524" layer="94"/>
<wire x1="2.54" y1="1.524" x2="2.54" y2="3.81" width="0.1524" layer="94"/>
<wire x1="-0.508" y1="-1.524" x2="2.54" y2="-1.524" width="0.1524" layer="94"/>
<wire x1="2.54" y1="-1.524" x2="2.54" y2="-3.81" width="0.1524" layer="94"/>
<wire x1="-0.508" y1="0" x2="2.54" y2="0" width="0.1524" layer="94"/>
<wire x1="2.54" y1="0" x2="2.54" y2="-1.524" width="0.1524" layer="94"/>
<wire x1="1.27" y1="0.508" x2="2.032" y2="0" width="0.254" layer="94"/>
<wire x1="2.032" y1="0" x2="1.27" y2="-0.508" width="0.254" layer="94"/>
<text x="4.5" y="1.8" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="4.5" y="-0.6" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<pin name="G" x="-5.08" y="0" length="short" direction="in"/>
<pin name="D" x="2.54" y="6.35" length="short" direction="pas" rot="R270"/>
<pin name="S" x="2.54" y="-6.35" length="short" direction="pas" rot="R90"/>
</symbol>
<symbol name="SWITCH-SPST">
<description>SPST momentary push-button (both lead pairs bonded)</description>
<wire x1="-2.54" y1="0" x2="-1.27" y2="0" width="0.1524" layer="94"/>
<wire x1="-1.27" y1="0.508" x2="1.524" y2="1.778" width="0.1524" layer="94"/>
<wire x1="1.27" y1="0" x2="2.54" y2="0" width="0.1524" layer="94"/>
<circle x="-1.27" y="0" radius="0.3" width="0.1524" layer="94"/>
<circle x="1.27" y="0" radius="0.3" width="0.1524" layer="94"/>
<wire x1="0" y1="1.9" x2="0" y2="3" width="0.1524" layer="94"/>
<wire x1="-1" y1="3" x2="1" y2="3" width="0.4" layer="94"/>
<text x="-2.54" y="4" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-2.54" y="-3" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<pin name="P" x="-5.08" y="0" length="short" direction="pas"/>
<pin name="N" x="5.08" y="0" length="short" direction="pas" rot="R180"/>
</symbol>
<symbol name="TESTPOINT">
<description>Test point</description>
<circle x="0" y="1.27" radius="0.5" width="0.254" layer="94"/>
<wire x1="0" y1="0" x2="0" y2="0.77" width="0.1524" layer="94"/>
<text x="1.4" y="0.5" size="1.524" layer="95" ratio="10">&gt;NAME</text>
<pin name="TP" x="0" y="-2.54" length="short" direction="pas" rot="R90"/>
</symbol>
<symbol name="MOUNTHOLE">
<description>Mounting hole (plated, GND-stitched)</description>
<circle x="0" y="0" radius="1.27" width="0.254" layer="94"/>
<circle x="0" y="0" radius="0.6" width="0.254" layer="94"/>
<text x="2" y="0.6" size="1.524" layer="95" ratio="10">&gt;NAME</text>
<pin name="1" x="-3.81" y="0" length="short" direction="pas"/>
</symbol>
<symbol name="CONN-2">
<description>2-way connector / header</description>
<wire x1="-6.35" y1="-3.81" x2="6.35" y2="-3.81" width="0.254" layer="94"/>
<wire x1="6.35" y1="-3.81" x2="6.35" y2="3.81" width="0.254" layer="94"/>
<wire x1="6.35" y1="3.81" x2="-6.35" y2="3.81" width="0.254" layer="94"/>
<wire x1="-6.35" y1="3.81" x2="-6.35" y2="-3.81" width="0.254" layer="94"/>
<text x="-6.35" y="4.61" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-6.35" y="-6.21" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<wire x1="5.35" y1="3.21" x2="6.35" y2="2.21" width="0.254" layer="94"/>
<pin name="1" x="-11.43" y="1.27" length="middle" direction="pas"/>
<text x="-5.65" y="0.72" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="2" x="-11.43" y="-1.27" length="middle" direction="pas"/>
<text x="-5.65" y="-1.82" size="0.9" layer="97" ratio="10">PAS</text>
</symbol>
<symbol name="CONN-3">
<description>3-way connector / header</description>
<wire x1="-6.35" y1="-5.08" x2="6.35" y2="-5.08" width="0.254" layer="94"/>
<wire x1="6.35" y1="-5.08" x2="6.35" y2="5.08" width="0.254" layer="94"/>
<wire x1="6.35" y1="5.08" x2="-6.35" y2="5.08" width="0.254" layer="94"/>
<wire x1="-6.35" y1="5.08" x2="-6.35" y2="-5.08" width="0.254" layer="94"/>
<text x="-6.35" y="5.88" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-6.35" y="-7.48" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<wire x1="5.35" y1="4.48" x2="6.35" y2="3.48" width="0.254" layer="94"/>
<pin name="1" x="-11.43" y="2.54" length="middle" direction="pas"/>
<text x="-5.65" y="1.99" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="2" x="-11.43" y="0" length="middle" direction="pas"/>
<text x="-5.65" y="-0.55" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="3" x="-11.43" y="-2.54" length="middle" direction="pas"/>
<text x="-5.65" y="-3.09" size="0.9" layer="97" ratio="10">PAS</text>
</symbol>
<symbol name="CONN-4">
<description>4-way connector / header</description>
<wire x1="-6.35" y1="-6.35" x2="6.35" y2="-6.35" width="0.254" layer="94"/>
<wire x1="6.35" y1="-6.35" x2="6.35" y2="6.35" width="0.254" layer="94"/>
<wire x1="6.35" y1="6.35" x2="-6.35" y2="6.35" width="0.254" layer="94"/>
<wire x1="-6.35" y1="6.35" x2="-6.35" y2="-6.35" width="0.254" layer="94"/>
<text x="-6.35" y="7.15" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-6.35" y="-8.75" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<wire x1="5.35" y1="5.75" x2="6.35" y2="4.75" width="0.254" layer="94"/>
<pin name="1" x="-11.43" y="3.81" length="middle" direction="pas"/>
<text x="-5.65" y="3.26" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="2" x="-11.43" y="1.27" length="middle" direction="pas"/>
<text x="-5.65" y="0.72" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="3" x="-11.43" y="-1.27" length="middle" direction="pas"/>
<text x="-5.65" y="-1.82" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="4" x="-11.43" y="-3.81" length="middle" direction="pas"/>
<text x="-5.65" y="-4.36" size="0.9" layer="97" ratio="10">PAS</text>
</symbol>
<symbol name="CONN-5">
<description>5-way connector / header</description>
<wire x1="-6.35" y1="-7.62" x2="6.35" y2="-7.62" width="0.254" layer="94"/>
<wire x1="6.35" y1="-7.62" x2="6.35" y2="7.62" width="0.254" layer="94"/>
<wire x1="6.35" y1="7.62" x2="-6.35" y2="7.62" width="0.254" layer="94"/>
<wire x1="-6.35" y1="7.62" x2="-6.35" y2="-7.62" width="0.254" layer="94"/>
<text x="-6.35" y="8.42" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-6.35" y="-10.02" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<wire x1="5.35" y1="7.02" x2="6.35" y2="6.02" width="0.254" layer="94"/>
<pin name="1" x="-11.43" y="5.08" length="middle" direction="pas"/>
<text x="-5.65" y="4.53" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="2" x="-11.43" y="2.54" length="middle" direction="pas"/>
<text x="-5.65" y="1.99" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="3" x="-11.43" y="0" length="middle" direction="pas"/>
<text x="-5.65" y="-0.55" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="4" x="-11.43" y="-2.54" length="middle" direction="pas"/>
<text x="-5.65" y="-3.09" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="5" x="-11.43" y="-5.08" length="middle" direction="pas"/>
<text x="-5.65" y="-5.63" size="0.9" layer="97" ratio="10">PAS</text>
</symbol>
<symbol name="CONN-6">
<description>6-way connector / header</description>
<wire x1="-6.35" y1="-8.89" x2="6.35" y2="-8.89" width="0.254" layer="94"/>
<wire x1="6.35" y1="-8.89" x2="6.35" y2="8.89" width="0.254" layer="94"/>
<wire x1="6.35" y1="8.89" x2="-6.35" y2="8.89" width="0.254" layer="94"/>
<wire x1="-6.35" y1="8.89" x2="-6.35" y2="-8.89" width="0.254" layer="94"/>
<text x="-6.35" y="9.69" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-6.35" y="-11.29" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<wire x1="5.35" y1="8.29" x2="6.35" y2="7.29" width="0.254" layer="94"/>
<pin name="1" x="-11.43" y="6.35" length="middle" direction="pas"/>
<text x="-5.65" y="5.8" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="2" x="-11.43" y="3.81" length="middle" direction="pas"/>
<text x="-5.65" y="3.26" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="3" x="-11.43" y="1.27" length="middle" direction="pas"/>
<text x="-5.65" y="0.72" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="4" x="-11.43" y="-1.27" length="middle" direction="pas"/>
<text x="-5.65" y="-1.82" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="5" x="-11.43" y="-3.81" length="middle" direction="pas"/>
<text x="-5.65" y="-4.36" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="6" x="-11.43" y="-6.35" length="middle" direction="pas"/>
<text x="-5.65" y="-6.9" size="0.9" layer="97" ratio="10">PAS</text>
</symbol>
<symbol name="CONN-8">
<description>8-way connector / header</description>
<wire x1="-6.35" y1="-11.43" x2="6.35" y2="-11.43" width="0.254" layer="94"/>
<wire x1="6.35" y1="-11.43" x2="6.35" y2="11.43" width="0.254" layer="94"/>
<wire x1="6.35" y1="11.43" x2="-6.35" y2="11.43" width="0.254" layer="94"/>
<wire x1="-6.35" y1="11.43" x2="-6.35" y2="-11.43" width="0.254" layer="94"/>
<text x="-6.35" y="12.23" size="1.778" layer="95" ratio="10">&gt;NAME</text>
<text x="-6.35" y="-13.83" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<wire x1="5.35" y1="10.83" x2="6.35" y2="9.83" width="0.254" layer="94"/>
<pin name="1" x="-11.43" y="8.89" length="middle" direction="pas"/>
<text x="-5.65" y="8.34" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="2" x="-11.43" y="6.35" length="middle" direction="pas"/>
<text x="-5.65" y="5.8" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="3" x="-11.43" y="3.81" length="middle" direction="pas"/>
<text x="-5.65" y="3.26" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="4" x="-11.43" y="1.27" length="middle" direction="pas"/>
<text x="-5.65" y="0.72" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="5" x="-11.43" y="-1.27" length="middle" direction="pas"/>
<text x="-5.65" y="-1.82" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="6" x="-11.43" y="-3.81" length="middle" direction="pas"/>
<text x="-5.65" y="-4.36" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="7" x="-11.43" y="-6.35" length="middle" direction="pas"/>
<text x="-5.65" y="-6.9" size="0.9" layer="97" ratio="10">PAS</text>
<pin name="8" x="-11.43" y="-8.89" length="middle" direction="pas"/>
<text x="-5.65" y="-9.44" size="0.9" layer="97" ratio="10">PAS</text>
</symbol>
<symbol name="SUPPLY-GND">
<description>GND supply rail marker</description>
<wire x1="-1.905" y1="0" x2="1.905" y2="0" width="0.254" layer="94"/>
<wire x1="-1.27" y1="-0.635" x2="1.27" y2="-0.635" width="0.254" layer="94"/>
<wire x1="-0.635" y1="-1.27" x2="0.635" y2="-1.27" width="0.254" layer="94"/>
<text x="-2.54" y="-3.4" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<pin name="GND" x="0" y="2.54" length="short" direction="sup" rot="R270" visible="off"/>
</symbol>
<symbol name="SUPPLY-AGND">
<description>AGND supply rail marker</description>
<wire x1="-1.905" y1="0" x2="1.905" y2="0" width="0.254" layer="94"/>
<wire x1="-1.27" y1="-0.635" x2="1.27" y2="-0.635" width="0.254" layer="94"/>
<wire x1="-0.635" y1="-1.27" x2="0.635" y2="-1.27" width="0.254" layer="94"/>
<text x="-2.54" y="-3.4" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<pin name="AGND" x="0" y="2.54" length="short" direction="sup" rot="R270" visible="off"/>
</symbol>
<symbol name="SUPPLY-3V3">
<description>3V3 supply rail marker</description>
<wire x1="-1.27" y1="1.27" x2="0" y2="2.54" width="0.254" layer="94"/>
<wire x1="0" y1="2.54" x2="1.27" y2="1.27" width="0.254" layer="94"/>
<wire x1="-1.27" y1="1.27" x2="1.27" y2="1.27" width="0.254" layer="94"/>
<text x="-2.54" y="3" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<pin name="3V3" x="0" y="0" length="short" direction="sup" rot="R90" visible="off"/>
</symbol>
<symbol name="SUPPLY-VBAT">
<description>VBAT supply rail marker</description>
<wire x1="-1.27" y1="1.27" x2="0" y2="2.54" width="0.254" layer="94"/>
<wire x1="0" y1="2.54" x2="1.27" y2="1.27" width="0.254" layer="94"/>
<wire x1="-1.27" y1="1.27" x2="1.27" y2="1.27" width="0.254" layer="94"/>
<text x="-2.54" y="3" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<pin name="VBAT" x="0" y="0" length="short" direction="sup" rot="R90" visible="off"/>
</symbol>
<symbol name="SUPPLY-VBUS">
<description>VBUS supply rail marker</description>
<wire x1="-1.27" y1="1.27" x2="0" y2="2.54" width="0.254" layer="94"/>
<wire x1="0" y1="2.54" x2="1.27" y2="1.27" width="0.254" layer="94"/>
<wire x1="-1.27" y1="1.27" x2="1.27" y2="1.27" width="0.254" layer="94"/>
<text x="-2.54" y="3" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<pin name="VBUS" x="0" y="0" length="short" direction="sup" rot="R90" visible="off"/>
</symbol>
<symbol name="SUPPLY-VCHG">
<description>VCHG supply rail marker</description>
<wire x1="-1.27" y1="1.27" x2="0" y2="2.54" width="0.254" layer="94"/>
<wire x1="0" y1="2.54" x2="1.27" y2="1.27" width="0.254" layer="94"/>
<wire x1="-1.27" y1="1.27" x2="1.27" y2="1.27" width="0.254" layer="94"/>
<text x="-2.54" y="3" size="1.778" layer="96" ratio="10">&gt;VALUE</text>
<pin name="VCHG" x="0" y="0" length="short" direction="sup" rot="R90" visible="off"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="ESP32-S3-WROOM-1" prefix="U" uservalue="no">
<description>Espressif ESP32-S3-WROOM-1-N8R2. Xtensa LX7 dual-core, Wi-Fi b/g/n + Bluetooth LE 5, 8 MB flash, 2 MB quad-SPI PSRAM, PCB antenna. Pin map from datasheet v1.8 Table 3-1. IO35/36/37 are free on the -N8R2 (quad PSRAM) variant only.</description>
<gates>
<gate name="G$1" symbol="ESP32-S3-WROOM-1" x="0" y="0"/>
</gates>
<devices>
<device name="" package="ESP32-S3-WROOM-1">
<connects>
<connect gate="G$1" pin="GND@1" pad="1"/>
<connect gate="G$1" pin="3V3" pad="2"/>
<connect gate="G$1" pin="EN" pad="3"/>
<connect gate="G$1" pin="IO4" pad="4"/>
<connect gate="G$1" pin="IO5" pad="5"/>
<connect gate="G$1" pin="IO6" pad="6"/>
<connect gate="G$1" pin="IO7" pad="7"/>
<connect gate="G$1" pin="IO15" pad="8"/>
<connect gate="G$1" pin="IO16" pad="9"/>
<connect gate="G$1" pin="IO17" pad="10"/>
<connect gate="G$1" pin="IO18" pad="11"/>
<connect gate="G$1" pin="IO8" pad="12"/>
<connect gate="G$1" pin="IO19" pad="13"/>
<connect gate="G$1" pin="IO20" pad="14"/>
<connect gate="G$1" pin="IO3" pad="15"/>
<connect gate="G$1" pin="IO46" pad="16"/>
<connect gate="G$1" pin="IO9" pad="17"/>
<connect gate="G$1" pin="IO10" pad="18"/>
<connect gate="G$1" pin="IO11" pad="19"/>
<connect gate="G$1" pin="IO12" pad="20"/>
<connect gate="G$1" pin="IO13" pad="21"/>
<connect gate="G$1" pin="IO14" pad="22"/>
<connect gate="G$1" pin="IO21" pad="23"/>
<connect gate="G$1" pin="IO47" pad="24"/>
<connect gate="G$1" pin="IO48" pad="25"/>
<connect gate="G$1" pin="IO45" pad="26"/>
<connect gate="G$1" pin="IO0" pad="27"/>
<connect gate="G$1" pin="IO35" pad="28"/>
<connect gate="G$1" pin="IO36" pad="29"/>
<connect gate="G$1" pin="IO37" pad="30"/>
<connect gate="G$1" pin="IO38" pad="31"/>
<connect gate="G$1" pin="IO39" pad="32"/>
<connect gate="G$1" pin="IO40" pad="33"/>
<connect gate="G$1" pin="IO41" pad="34"/>
<connect gate="G$1" pin="IO42" pad="35"/>
<connect gate="G$1" pin="RXD0" pad="36"/>
<connect gate="G$1" pin="TXD0" pad="37"/>
<connect gate="G$1" pin="IO2" pad="38"/>
<connect gate="G$1" pin="IO1" pad="39"/>
<connect gate="G$1" pin="GND@40" pad="40"/>
<connect gate="G$1" pin="EPAD" pad="41"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="AD8232" prefix="U" uservalue="no">
<description>Analog Devices AD8232ACPZ-R7 single-lead heart-rate monitor front end. Supply 2.0-3.5 V. Pin map from AD8232 Rev.A Table 3.</description>
<gates>
<gate name="G$1" symbol="AD8232" x="0" y="0"/>
</gates>
<devices>
<device name="" package="LFCSP-20-4X4-P050">
<connects>
<connect gate="G$1" pin="HPDRIVE" pad="1"/>
<connect gate="G$1" pin="+IN" pad="2"/>
<connect gate="G$1" pin="-IN" pad="3"/>
<connect gate="G$1" pin="RLDFB" pad="4"/>
<connect gate="G$1" pin="RLD" pad="5"/>
<connect gate="G$1" pin="SW" pad="6"/>
<connect gate="G$1" pin="OPAMP+" pad="7"/>
<connect gate="G$1" pin="REFOUT" pad="8"/>
<connect gate="G$1" pin="OPAMP-" pad="9"/>
<connect gate="G$1" pin="OUT" pad="10"/>
<connect gate="G$1" pin="LOD-" pad="11"/>
<connect gate="G$1" pin="LOD+" pad="12"/>
<connect gate="G$1" pin="SDN" pad="13"/>
<connect gate="G$1" pin="AC/DC" pad="14"/>
<connect gate="G$1" pin="FR" pad="15"/>
<connect gate="G$1" pin="GND" pad="16"/>
<connect gate="G$1" pin="+VS" pad="17"/>
<connect gate="G$1" pin="REFIN" pad="18"/>
<connect gate="G$1" pin="IAOUT" pad="19"/>
<connect gate="G$1" pin="HPSENSE" pad="20"/>
<connect gate="G$1" pin="EP" pad="EP"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="TMP117" prefix="U" uservalue="no">
<description>TI TMP117AIDRVR high-accuracy digital temperature sensor, WSON-6 (DRV). +/-0.1 C, 1.8-5.5 V, I2C. Pin map from TMP117 SNOSD82D Table 5-1 (WSON column).</description>
<gates>
<gate name="G$1" symbol="TMP117" x="0" y="0"/>
</gates>
<devices>
<device name="" package="WSON-6-DRV0006B">
<connects>
<connect gate="G$1" pin="SCL" pad="1"/>
<connect gate="G$1" pin="GND" pad="2"/>
<connect gate="G$1" pin="ALERT" pad="3"/>
<connect gate="G$1" pin="ADD0" pad="4"/>
<connect gate="G$1" pin="V+" pad="5"/>
<connect gate="G$1" pin="SDA" pad="6"/>
<connect gate="G$1" pin="TPAD" pad="7"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="LSM6DSOX" prefix="U" uservalue="no">
<description>ST LSM6DSOXTR 6-axis IMU (3-axis accel + 3-axis gyro), LGA-14L. Pin map from LSM6DSOX DS12814 Rev.4 Table 1.</description>
<gates>
<gate name="G$1" symbol="LSM6DSOX" x="0" y="0"/>
</gates>
<devices>
<device name="" package="LGA-14L-2.5X3.0">
<connects>
<connect gate="G$1" pin="SDO/SA0" pad="1"/>
<connect gate="G$1" pin="SDx" pad="2"/>
<connect gate="G$1" pin="SCx" pad="3"/>
<connect gate="G$1" pin="INT1" pad="4"/>
<connect gate="G$1" pin="VDDIO" pad="5"/>
<connect gate="G$1" pin="GND@6" pad="6"/>
<connect gate="G$1" pin="GND@7" pad="7"/>
<connect gate="G$1" pin="VDD" pad="8"/>
<connect gate="G$1" pin="INT2" pad="9"/>
<connect gate="G$1" pin="OCS_AUX" pad="10"/>
<connect gate="G$1" pin="SDO_AUX" pad="11"/>
<connect gate="G$1" pin="CS" pad="12"/>
<connect gate="G$1" pin="SCL" pad="13"/>
<connect gate="G$1" pin="SDA" pad="14"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="AS5600" prefix="U" uservalue="no">
<description>ams-OSRAM AS5600-ASOM 12-bit contactless magnetic rotary position sensor, SOIC-8. Fixed I2C address 0x36. Pin map from AS5600 DS000365 v1-06 Figure 4.</description>
<gates>
<gate name="G$1" symbol="AS5600" x="0" y="0"/>
</gates>
<devices>
<device name="" package="SOIC-8-N">
<connects>
<connect gate="G$1" pin="VDD5V" pad="1"/>
<connect gate="G$1" pin="VDD3V3" pad="2"/>
<connect gate="G$1" pin="OUT" pad="3"/>
<connect gate="G$1" pin="GND" pad="4"/>
<connect gate="G$1" pin="PGO" pad="5"/>
<connect gate="G$1" pin="SDA" pad="6"/>
<connect gate="G$1" pin="SCL" pad="7"/>
<connect gate="G$1" pin="DIR" pad="8"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="TP4056" prefix="U" uservalue="no">
<description>NanJing Top Power TP4056-42-SOP8-PP 1 A standalone linear Li-ion charger, 4.2 V float. Pin map from the TP4056 datasheet pin description (page 2).</description>
<gates>
<gate name="G$1" symbol="TP4056" x="0" y="0"/>
</gates>
<devices>
<device name="" package="SOIC-8-N">
<connects>
<connect gate="G$1" pin="TEMP" pad="1"/>
<connect gate="G$1" pin="PROG" pad="2"/>
<connect gate="G$1" pin="GND" pad="3"/>
<connect gate="G$1" pin="VCC" pad="4"/>
<connect gate="G$1" pin="BAT" pad="5"/>
<connect gate="G$1" pin="STDBY" pad="6"/>
<connect gate="G$1" pin="CHRG" pad="7"/>
<connect gate="G$1" pin="CE" pad="8"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="AP2112K-3.3" prefix="U" uservalue="no">
<description>Diodes AP2112K-3.3TRG1 600 mA CMOS LDO, fixed 3.3 V, with enable. Pin map from AP2112 DS39724 Rev.2-2 pin descriptions (SOT25 column).</description>
<gates>
<gate name="G$1" symbol="AP2112K" x="0" y="0"/>
</gates>
<devices>
<device name="" package="SOT-23-5">
<connects>
<connect gate="G$1" pin="VOUT" pad="5"/>
<connect gate="G$1" pin="GND" pad="2"/>
<connect gate="G$1" pin="EN" pad="3"/>
<connect gate="G$1" pin="NC" pad="4"/>
<connect gate="G$1" pin="VIN" pad="1"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="HX711" prefix="U" uservalue="no">
<description>Avia Semiconductor HX711 24-bit ADC for bridge sensors, SOP-16L. Pin map from the HX711 English datasheet Table 1.</description>
<gates>
<gate name="G$1" symbol="HX711" x="0" y="0"/>
</gates>
<devices>
<device name="" package="SOP-16-N">
<connects>
<connect gate="G$1" pin="VSUP" pad="1"/>
<connect gate="G$1" pin="BASE" pad="2"/>
<connect gate="G$1" pin="AVDD" pad="3"/>
<connect gate="G$1" pin="VFB" pad="4"/>
<connect gate="G$1" pin="AGND" pad="5"/>
<connect gate="G$1" pin="VBG" pad="6"/>
<connect gate="G$1" pin="INA-" pad="7"/>
<connect gate="G$1" pin="INA+" pad="8"/>
<connect gate="G$1" pin="INB-" pad="9"/>
<connect gate="G$1" pin="INB+" pad="10"/>
<connect gate="G$1" pin="PD_SCK" pad="11"/>
<connect gate="G$1" pin="DOUT" pad="12"/>
<connect gate="G$1" pin="XO" pad="13"/>
<connect gate="G$1" pin="XI" pad="14"/>
<connect gate="G$1" pin="RATE" pad="15"/>
<connect gate="G$1" pin="DVDD" pad="16"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="R-0805" prefix="R" uservalue="yes">
<description>Chip resistor, 0805 (2012 metric)</description>
<gates>
<gate name="G$1" symbol="R" x="0" y="0"/>
</gates>
<devices>
<device name="" package="R0805">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="C-0805" prefix="C" uservalue="yes">
<description>Chip capacitor, 0805 (2012 metric)</description>
<gates>
<gate name="G$1" symbol="C" x="0" y="0"/>
</gates>
<devices>
<device name="" package="C0805">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="LED-0805" prefix="D" uservalue="yes">
<description>Chip LED, 0805. Pad 1 = cathode.</description>
<gates>
<gate name="G$1" symbol="LED" x="0" y="0"/>
</gates>
<devices>
<device name="" package="LED0805">
<connects>
<connect gate="G$1" pin="C" pad="1"/>
<connect gate="G$1" pin="A" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="DIODE-SOD123" prefix="D" uservalue="yes">
<description>Schottky/rectifier diode, SOD-123. Pad 1 = cathode (band).</description>
<gates>
<gate name="G$1" symbol="DIODE" x="0" y="0"/>
</gates>
<devices>
<device name="" package="SOD-123">
<connects>
<connect gate="G$1" pin="C" pad="1"/>
<connect gate="G$1" pin="A" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="NMOS-SOT23" prefix="Q" uservalue="yes">
<description>N-channel logic-level MOSFET, SOT-23-3. Standard assignment 1 = Gate, 2 = Source, 3 = Drain.</description>
<gates>
<gate name="G$1" symbol="NMOS" x="0" y="0"/>
</gates>
<devices>
<device name="" package="SOT-23-3">
<connects>
<connect gate="G$1" pin="G" pad="1"/>
<connect gate="G$1" pin="S" pad="2"/>
<connect gate="G$1" pin="D" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="SW-TACT-6MM" prefix="SW" uservalue="yes">
<description>6 x 6 mm through-hole tactile push-button. Leads 1-2 and 3-4 are internally common, so each symbol pin maps to two pads (EAGLE multi-pad connect).</description>
<gates>
<gate name="G$1" symbol="SWITCH-SPST" x="0" y="0"/>
</gates>
<devices>
<device name="" package="TACT-6X6-THT">
<connects>
<connect gate="G$1" pin="P" pad="1 2"/>
<connect gate="G$1" pin="N" pad="3 4"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="TESTPOINT" prefix="TP" uservalue="no">
<description>1.5 mm SMD test point</description>
<gates>
<gate name="G$1" symbol="TESTPOINT" x="0" y="0"/>
</gates>
<devices>
<device name="" package="TESTPOINT-1.5">
<connects>
<connect gate="G$1" pin="TP" pad="TP"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="MOUNTHOLE-M2" prefix="H" uservalue="no">
<description>M2 plated mounting hole, GND-stitched</description>
<gates>
<gate name="G$1" symbol="MOUNTHOLE" x="0" y="0"/>
</gates>
<devices>
<device name="" package="MOUNT-M2">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="JST-PH-2" prefix="J" uservalue="yes">
<description>JST PH 2.00 mm 2-circuit top-entry header (S2B-PH-K-S). Li-Po battery input.</description>
<gates>
<gate name="G$1" symbol="CONN-2" x="0" y="0"/>
</gates>
<devices>
<device name="" package="JST-PH-2">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="JST-PH-4" prefix="J" uservalue="yes">
<description>JST PH 2.00 mm 4-circuit top-entry header (S4B-PH-K-S). Load-cell bridge input.</description>
<gates>
<gate name="G$1" symbol="CONN-4" x="0" y="0"/>
</gates>
<devices>
<device name="" package="JST-PH-4">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="4" pad="4"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="HDR-1X2" prefix="J" uservalue="yes">
<description>1x2 2.54 mm pin header</description>
<gates>
<gate name="G$1" symbol="CONN-2" x="0" y="0"/>
</gates>
<devices>
<device name="" package="HDR-1X2">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="HDR-1X3" prefix="J" uservalue="yes">
<description>1x3 2.54 mm pin header</description>
<gates>
<gate name="G$1" symbol="CONN-3" x="0" y="0"/>
</gates>
<devices>
<device name="" package="HDR-1X3">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="HDR-1X4" prefix="J" uservalue="yes">
<description>1x4 2.54 mm pin header</description>
<gates>
<gate name="G$1" symbol="CONN-4" x="0" y="0"/>
</gates>
<devices>
<device name="" package="HDR-1X4">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="4" pad="4"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="HDR-1X5" prefix="J" uservalue="yes">
<description>1x5 2.54 mm pin header</description>
<gates>
<gate name="G$1" symbol="CONN-5" x="0" y="0"/>
</gates>
<devices>
<device name="" package="HDR-1X5">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="4" pad="4"/>
<connect gate="G$1" pin="5" pad="5"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="HDR-1X6" prefix="J" uservalue="yes">
<description>1x6 2.54 mm pin header</description>
<gates>
<gate name="G$1" symbol="CONN-6" x="0" y="0"/>
</gates>
<devices>
<device name="" package="HDR-1X6">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="4" pad="4"/>
<connect gate="G$1" pin="5" pad="5"/>
<connect gate="G$1" pin="6" pad="6"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="HDR-1X8" prefix="J" uservalue="yes">
<description>1x8 2.54 mm pin header</description>
<gates>
<gate name="G$1" symbol="CONN-8" x="0" y="0"/>
</gates>
<devices>
<device name="" package="HDR-1X8">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="4" pad="4"/>
<connect gate="G$1" pin="5" pad="5"/>
<connect gate="G$1" pin="6" pad="6"/>
<connect gate="G$1" pin="7" pad="7"/>
<connect gate="G$1" pin="8" pad="8"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="SUPPLY-GND" prefix="SUPPLY" uservalue="no">
<description>GND rail symbol</description>
<gates>
<gate name="G$1" symbol="SUPPLY-GND" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="SUPPLY-AGND" prefix="SUPPLY" uservalue="no">
<description>AGND rail symbol</description>
<gates>
<gate name="G$1" symbol="SUPPLY-AGND" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="SUPPLY-3V3" prefix="SUPPLY" uservalue="no">
<description>3V3 rail symbol</description>
<gates>
<gate name="G$1" symbol="SUPPLY-3V3" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="SUPPLY-VBAT" prefix="SUPPLY" uservalue="no">
<description>VBAT rail symbol</description>
<gates>
<gate name="G$1" symbol="SUPPLY-VBAT" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="SUPPLY-VBUS" prefix="SUPPLY" uservalue="no">
<description>VBUS rail symbol</description>
<gates>
<gate name="G$1" symbol="SUPPLY-VBUS" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="SUPPLY-VCHG" prefix="SUPPLY" uservalue="no">
<description>VCHG rail symbol</description>
<gates>
<gate name="G$1" symbol="SUPPLY-VCHG" x="0" y="0"/>
</gates>
<devices>
<device name="">
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes/>
<variantdefs/>
<classes>
<class number="0" name="default" width="0.2" drill="0.3">
<clearance class="0" value="0.15"/>
</class>
<class number="1" name="power" width="0.5" drill="0.4">
<clearance class="1" value="0.2"/>
</class>
<class number="2" name="motor" width="0.5" drill="0.4">
<clearance class="2" value="0.2"/>
</class>
<class number="3" name="analog_ecg" width="0.2" drill="0.3">
<clearance class="3" value="0.2"/>
</class>
</classes>
<parts>
<part name="C1" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10u"/>
<part name="C2" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10u"/>
<part name="C3" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10u"/>
<part name="C4" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10u"/>
<part name="C5" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="C6" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="D1" library="SIH26113_Maternity_Assist_Belt" deviceset="LED-0805" device="" value="RED"/>
<part name="D2" library="SIH26113_Maternity_Assist_Belt" deviceset="LED-0805" device="" value="GRN"/>
<part name="H1" library="SIH26113_Maternity_Assist_Belt" deviceset="MOUNTHOLE-M2" device="" value="M2"/>
<part name="H2" library="SIH26113_Maternity_Assist_Belt" deviceset="MOUNTHOLE-M2" device="" value="M2"/>
<part name="H3" library="SIH26113_Maternity_Assist_Belt" deviceset="MOUNTHOLE-M2" device="" value="M2"/>
<part name="H4" library="SIH26113_Maternity_Assist_Belt" deviceset="MOUNTHOLE-M2" device="" value="M2"/>
<part name="J1" library="SIH26113_Maternity_Assist_Belt" deviceset="JST-PH-2" device="" value="LI-PO 3.7V"/>
<part name="J2" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X4" device="" value="USB / 5V IN"/>
<part name="J3" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X2" device="" value="OFF SW"/>
<part name="J4" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X5" device="" value="FUEL GAUGE"/>
<part name="R1" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="2k4"/>
<part name="R2" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="1k"/>
<part name="R3" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="1k"/>
<part name="R4" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="100k"/>
<part name="R5" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="470k"/>
<part name="R6" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="470k"/>
<part name="SUPPLY1" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-GND" device="" value="GND"/>
<part name="SUPPLY2" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-VBAT" device="" value="VBAT"/>
<part name="SUPPLY3" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-VBUS" device="" value="VBUS"/>
<part name="SUPPLY4" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-3V3" device="" value="3V3"/>
<part name="TP1" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="VBAT"/>
<part name="TP2" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="3V3"/>
<part name="TP3" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="GND"/>
<part name="TP4" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="VBUS"/>
<part name="U1" library="SIH26113_Maternity_Assist_Belt" deviceset="TP4056" device="" value="TP4056"/>
<part name="U2" library="SIH26113_Maternity_Assist_Belt" deviceset="AP2112K-3.3" device="" value="AP2112K-3.3"/>
<part name="C10" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="1u"/>
<part name="C7" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="C8" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="22u"/>
<part name="D3" library="SIH26113_Maternity_Assist_Belt" deviceset="LED-0805" device="" value="GRN"/>
<part name="D4" library="SIH26113_Maternity_Assist_Belt" deviceset="LED-0805" device="" value="RED"/>
<part name="J5" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X6" device="" value="UART PROG"/>
<part name="R10" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="1k"/>
<part name="R7" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10k"/>
<part name="R8" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10k"/>
<part name="R9" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="1k"/>
<part name="SUPPLY5" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-GND" device="" value="GND"/>
<part name="SUPPLY6" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-3V3" device="" value="3V3"/>
<part name="SW2" library="SIH26113_Maternity_Assist_Belt" deviceset="SW-TACT-6MM" device="" value="RESET"/>
<part name="SW3" library="SIH26113_Maternity_Assist_Belt" deviceset="SW-TACT-6MM" device="" value="BOOT"/>
<part name="TP5" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="IO3"/>
<part name="TP6" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="TMP_ALERT"/>
<part name="U3" library="SIH26113_Maternity_Assist_Belt" deviceset="ESP32-S3-WROOM-1" device="" value="ESP32-S3-WROOM-1-N8R2"/>
<part name="C11" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="C12" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="C13" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="C14" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="C15" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="1u"/>
<part name="J6" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X5" device="" value="AS5600 SIDE-B"/>
<part name="R11" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="4k7"/>
<part name="R12" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="4k7"/>
<part name="R13" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10k"/>
<part name="R15" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="4k7"/>
<part name="R16" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="4k7"/>
<part name="R17" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="0R DNP"/>
<part name="SUPPLY7" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-GND" device="" value="GND"/>
<part name="SUPPLY8" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-3V3" device="" value="3V3"/>
<part name="TP7" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="IMU_INT1"/>
<part name="TP8" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="AS_OUT"/>
<part name="TP9" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="AS_PGO"/>
<part name="U4" library="SIH26113_Maternity_Assist_Belt" deviceset="TMP117" device="" value="TMP117"/>
<part name="U5" library="SIH26113_Maternity_Assist_Belt" deviceset="LSM6DSOX" device="" value="LSM6DSOX"/>
<part name="U6" library="SIH26113_Maternity_Assist_Belt" deviceset="AS5600" device="" value="AS5600"/>
<part name="C16" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="C17" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="1n"/>
<part name="C18" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="220n"/>
<part name="C19" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="220n"/>
<part name="C20" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="8n2"/>
<part name="C21" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="3n9"/>
<part name="C22" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10n"/>
<part name="C23" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="C24" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="1u"/>
<part name="J7" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X3" device="" value="ECG ELECTRODES"/>
<part name="R18" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="330k"/>
<part name="R19" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="330k"/>
<part name="R20" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="330k"/>
<part name="R21" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10M"/>
<part name="R22" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10M"/>
<part name="R23" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10M"/>
<part name="R24" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10M"/>
<part name="R25" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10M"/>
<part name="R26" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="1M"/>
<part name="R27" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="470k"/>
<part name="R28" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="100k"/>
<part name="R29" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="1M"/>
<part name="R30" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="1k"/>
<part name="R31" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="100k"/>
<part name="R32" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="100k"/>
<part name="SUPPLY10" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-3V3" device="" value="3V3"/>
<part name="SUPPLY9" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-GND" device="" value="GND"/>
<part name="TP10" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="ECG_OUT"/>
<part name="TP11" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="ECG_REF"/>
<part name="U7" library="SIH26113_Maternity_Assist_Belt" deviceset="AD8232" device="" value="AD8232"/>
<part name="C25" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="C26" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="C27" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="C28" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10u"/>
<part name="C29" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10n"/>
<part name="C30" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10n"/>
<part name="C31" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10n"/>
<part name="C32" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10n"/>
<part name="C33" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10n"/>
<part name="C34" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n/50V"/>
<part name="C35" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10n"/>
<part name="C36" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="D5" library="SIH26113_Maternity_Assist_Belt" deviceset="DIODE-SOD123" device="" value="1N5819HW"/>
<part name="D6" library="SIH26113_Maternity_Assist_Belt" deviceset="DIODE-SOD123" device="" value="1N5819HW"/>
<part name="J10" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X2" device="" value="FSR2"/>
<part name="J11" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X2" device="" value="FSR3"/>
<part name="J12" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X2" device="" value="FSR4"/>
<part name="J13" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X2" device="" value="STRETCH"/>
<part name="J14" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X2" device="" value="PIEZO"/>
<part name="J15" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X3" device="" value="HALL / LIMIT"/>
<part name="J8" library="SIH26113_Maternity_Assist_Belt" deviceset="JST-PH-4" device="" value="LOAD CELL"/>
<part name="J9" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X2" device="" value="FSR1"/>
<part name="R33" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10k"/>
<part name="R34" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10k"/>
<part name="R35" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10k"/>
<part name="R36" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10k"/>
<part name="R37" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10k"/>
<part name="R38" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10M"/>
<part name="R39" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="1M"/>
<part name="R40" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="1M"/>
<part name="R41" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="100k"/>
<part name="R42" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10k"/>
<part name="SUPPLY11" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-GND" device="" value="GND"/>
<part name="SUPPLY12" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-3V3" device="" value="3V3"/>
<part name="TP12" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="HX_BASE"/>
<part name="TP13" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="HX_XO"/>
<part name="TP14" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="HX_DOUT"/>
<part name="U8" library="SIH26113_Maternity_Assist_Belt" deviceset="HX711" device="" value="HX711"/>
<part name="C37" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10u"/>
<part name="C38" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="10u"/>
<part name="D7" library="SIH26113_Maternity_Assist_Belt" deviceset="DIODE-SOD123" device="" value="1N5819HW"/>
<part name="D8" library="SIH26113_Maternity_Assist_Belt" deviceset="DIODE-SOD123" device="" value="1N5819HW"/>
<part name="J16" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X2" device="" value="VIB MOTOR"/>
<part name="J17" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X2" device="" value="BUZZER"/>
<part name="Q1" library="SIH26113_Maternity_Assist_Belt" deviceset="NMOS-SOT23" device="" value="AO3400A"/>
<part name="Q2" library="SIH26113_Maternity_Assist_Belt" deviceset="NMOS-SOT23" device="" value="AO3400A"/>
<part name="R43" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="100R"/>
<part name="R44" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="100k"/>
<part name="R45" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="0R"/>
<part name="R46" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="100R"/>
<part name="R47" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="100k"/>
<part name="SUPPLY13" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-GND" device="" value="GND"/>
<part name="SUPPLY14" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-3V3" device="" value="3V3"/>
<part name="SUPPLY15" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-VBAT" device="" value="VBAT"/>
<part name="TP15" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="MOTOR_EN"/>
<part name="TP16" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="BUZZER_EN"/>
<part name="C39" library="SIH26113_Maternity_Assist_Belt" deviceset="C-0805" device="" value="100n"/>
<part name="J18" library="SIH26113_Maternity_Assist_Belt" deviceset="HDR-1X6" device="" value="MICROSD SPI"/>
<part name="R48" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10k"/>
<part name="R49" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="1k"/>
<part name="R50" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10k"/>
<part name="R51" library="SIH26113_Maternity_Assist_Belt" deviceset="R-0805" device="" value="10k"/>
<part name="SUPPLY16" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-GND" device="" value="GND"/>
<part name="SUPPLY17" library="SIH26113_Maternity_Assist_Belt" deviceset="SUPPLY-3V3" device="" value="3V3"/>
<part name="SW4" library="SIH26113_Maternity_Assist_Belt" deviceset="SW-TACT-6MM" device="" value="SOS"/>
<part name="TP17" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="SOS_GPIO"/>
<part name="TP18" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="I2C_SDA"/>
<part name="TP19" library="SIH26113_Maternity_Assist_Belt" deviceset="TESTPOINT" device="" value="I2C_SCL"/>
</parts>
<sheets>
<sheet>
<description>SHEET 1/7 - POWER ENTRY, CHARGING AND 3V3 REGULATION</description>
<plain>
<wire x1="0" y1="0" x2="380" y2="0" width="0.3" layer="94"/>
<wire x1="380" y1="0" x2="380" y2="260" width="0.3" layer="94"/>
<wire x1="380" y1="260" x2="0" y2="260" width="0.3" layer="94"/>
<wire x1="0" y1="260" x2="0" y2="0" width="0.3" layer="94"/>
<wire x1="0" y1="22" x2="380" y2="22" width="0.3" layer="94"/>
<wire x1="0" y1="10" x2="380" y2="10" width="0.2" layer="94"/>
<text x="3" y="16" size="3" layer="94" ratio="10">SIH26113 - MATERNITY ASSIST BELT - PROTOTYPE CARRIER BOARD</text>
<text x="3" y="12" size="2" layer="94" ratio="10">SHEET 1/7 - POWER ENTRY, CHARGING AND 3V3 REGULATION</text>
<text x="3" y="5.5" size="1.8" layer="94" ratio="10">NOT A MEDICAL DEVICE. Prototype for engineering evaluation only. Human-connected ECG is NOT isolated - see documentation/README.</text>
<text x="3" y="2" size="1.8" layer="94" ratio="10">4-layer FR-4 1.6 mm (L1 sig / L2 GND plane / L15 3V3 plane / L16 sig) | board 100 x 70 mm | lib SIH26113_Maternity_Assist_Belt.lbr | sheet 1 of 7</text>
<text x="320" y="252" size="3.5" layer="94" ratio="10">SHEET 1/7</text>
<text x="20" y="200" size="2.6" layer="94" ratio="10">BATTERY / CHARGE INPUT</text>
<text x="95" y="200" size="2.6" layer="94" ratio="10">TP4056 CHARGER</text>
<text x="150" y="200" size="2.6" layer="94" ratio="10">3V3 LDO</text>
<text x="200" y="200" size="2.6" layer="94" ratio="10">BATTERY MONITOR</text>
</plain>
<instances>
<instance part="J1" gate="G$1" x="25" y="175"/>
<instance part="J2" gate="G$1" x="25" y="140"/>
<instance part="U1" gate="G$1" x="80" y="160"/>
<instance part="R1" gate="G$1" x="70" y="140" rot="R90"/>
<instance part="R2" gate="G$1" x="105" y="178"/>
<instance part="R3" gate="G$1" x="105" y="170"/>
<instance part="D1" gate="G$1" x="118" y="178"/>
<instance part="D2" gate="G$1" x="118" y="170"/>
<instance part="C1" gate="G$1" x="45" y="145"/>
<instance part="C2" gate="G$1" x="100" y="140"/>
<instance part="U2" gate="G$1" x="150" y="160"/>
<instance part="R4" gate="G$1" x="138" y="145" rot="R90"/>
<instance part="J3" gate="G$1" x="130" y="120"/>
<instance part="C3" gate="G$1" x="138" y="172"/>
<instance part="C4" gate="G$1" x="172" y="172"/>
<instance part="C5" gate="G$1" x="182" y="172"/>
<instance part="R5" gate="G$1" x="205" y="175" rot="R90"/>
<instance part="R6" gate="G$1" x="205" y="160" rot="R90"/>
<instance part="C6" gate="G$1" x="218" y="160"/>
<instance part="J4" gate="G$1" x="205" y="120"/>
<instance part="TP1" gate="G$1" x="240" y="178"/>
<instance part="TP2" gate="G$1" x="250" y="178"/>
<instance part="TP3" gate="G$1" x="260" y="178"/>
<instance part="TP4" gate="G$1" x="270" y="178"/>
<instance part="H1" gate="G$1" x="240" y="130"/>
<instance part="H2" gate="G$1" x="252" y="130"/>
<instance part="H3" gate="G$1" x="264" y="130"/>
<instance part="H4" gate="G$1" x="276" y="130"/>
<instance part="SUPPLY1" gate="G$1" x="30" y="100"/>
<instance part="SUPPLY2" gate="G$1" x="45" y="100"/>
<instance part="SUPPLY3" gate="G$1" x="60" y="100"/>
<instance part="SUPPLY4" gate="G$1" x="75" y="100"/>
</instances>
<busses/>
<nets>
<net name="3V3" class="1">
<segment>
<pinref part="SUPPLY4" gate="G$1" pin="3V3"/>
<wire x1="75" y1="100" x2="75" y2="96.19" width="0.1524" layer="91"/>
<label x="75" y="96.99" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U2" gate="G$1" pin="VOUT"/>
<wire x1="166.51" y1="162.54" x2="170.32" y2="162.54" width="0.1524" layer="91"/>
<label x="171.12" y="163.34" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C4" gate="G$1" pin="1"/>
<wire x1="172" y1="177.08" x2="172" y2="180.89" width="0.1524" layer="91"/>
<label x="172" y="181.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C5" gate="G$1" pin="1"/>
<wire x1="182" y1="177.08" x2="182" y2="180.89" width="0.1524" layer="91"/>
<label x="182" y="181.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J4" gate="G$1" pin="3"/>
<wire x1="193.57" y1="120" x2="189.76" y2="120" width="0.1524" layer="91"/>
<label x="188.96" y="120.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="TP2" gate="G$1" pin="TP"/>
<wire x1="250" y1="175.46" x2="250" y2="171.65" width="0.1524" layer="91"/>
<label x="250" y="172.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="CHG_PROG" class="0">
<segment>
<pinref part="U1" gate="G$1" pin="PROG"/>
<wire x1="97.78" y1="161.27" x2="101.59" y2="161.27" width="0.1524" layer="91"/>
<label x="102.39" y="162.07" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R1" gate="G$1" pin="1"/>
<wire x1="70" y1="134.92" x2="70" y2="131.11" width="0.1524" layer="91"/>
<label x="70" y="131.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="GND" class="1">
<segment>
<pinref part="SUPPLY1" gate="G$1" pin="GND"/>
<wire x1="30" y1="102.54" x2="30" y2="106.35" width="0.1524" layer="91"/>
<label x="30" y="107.15" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J1" gate="G$1" pin="2"/>
<wire x1="13.57" y1="173.73" x2="9.76" y2="173.73" width="0.1524" layer="91"/>
<label x="8.96" y="174.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="J2" gate="G$1" pin="4"/>
<wire x1="13.57" y1="136.19" x2="9.76" y2="136.19" width="0.1524" layer="91"/>
<label x="8.96" y="136.99" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U1" gate="G$1" pin="GND"/>
<wire x1="62.22" y1="161.27" x2="58.41" y2="161.27" width="0.1524" layer="91"/>
<label x="57.61" y="162.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R1" gate="G$1" pin="2"/>
<wire x1="70" y1="145.08" x2="70" y2="148.89" width="0.1524" layer="91"/>
<label x="70" y="149.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C1" gate="G$1" pin="2"/>
<wire x1="45" y1="139.92" x2="45" y2="136.11" width="0.1524" layer="91"/>
<label x="45" y="136.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C2" gate="G$1" pin="2"/>
<wire x1="100" y1="134.92" x2="100" y2="131.11" width="0.1524" layer="91"/>
<label x="100" y="131.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U2" gate="G$1" pin="GND"/>
<wire x1="133.49" y1="160" x2="129.68" y2="160" width="0.1524" layer="91"/>
<label x="128.88" y="160.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="J3" gate="G$1" pin="2"/>
<wire x1="118.57" y1="118.73" x2="114.76" y2="118.73" width="0.1524" layer="91"/>
<label x="113.96" y="119.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="C3" gate="G$1" pin="2"/>
<wire x1="138" y1="166.92" x2="138" y2="163.11" width="0.1524" layer="91"/>
<label x="138" y="163.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C4" gate="G$1" pin="2"/>
<wire x1="172" y1="166.92" x2="172" y2="163.11" width="0.1524" layer="91"/>
<label x="172" y="163.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C5" gate="G$1" pin="2"/>
<wire x1="182" y1="166.92" x2="182" y2="163.11" width="0.1524" layer="91"/>
<label x="182" y="163.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R6" gate="G$1" pin="2"/>
<wire x1="205" y1="165.08" x2="205" y2="168.89" width="0.1524" layer="91"/>
<label x="205" y="169.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C6" gate="G$1" pin="2"/>
<wire x1="218" y1="154.92" x2="218" y2="151.11" width="0.1524" layer="91"/>
<label x="218" y="151.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J4" gate="G$1" pin="2"/>
<wire x1="193.57" y1="122.54" x2="189.76" y2="122.54" width="0.1524" layer="91"/>
<label x="188.96" y="123.34" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="TP3" gate="G$1" pin="TP"/>
<wire x1="260" y1="175.46" x2="260" y2="171.65" width="0.1524" layer="91"/>
<label x="260" y="172.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="H1" gate="G$1" pin="1"/>
<wire x1="236.19" y1="130" x2="232.38" y2="130" width="0.1524" layer="91"/>
<label x="231.58" y="130.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="H2" gate="G$1" pin="1"/>
<wire x1="248.19" y1="130" x2="244.38" y2="130" width="0.1524" layer="91"/>
<label x="243.58" y="130.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="H3" gate="G$1" pin="1"/>
<wire x1="260.19" y1="130" x2="256.38" y2="130" width="0.1524" layer="91"/>
<label x="255.58" y="130.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="H4" gate="G$1" pin="1"/>
<wire x1="272.19" y1="130" x2="268.38" y2="130" width="0.1524" layer="91"/>
<label x="267.58" y="130.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U1" gate="G$1" pin="TEMP"/>
<wire x1="62.22" y1="156.19" x2="58.41" y2="156.19" width="0.1524" layer="91"/>
<label x="57.61" y="156.99" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="I2C_SCL" class="0">
<segment>
<pinref part="J4" gate="G$1" pin="5"/>
<wire x1="193.57" y1="114.92" x2="189.76" y2="114.92" width="0.1524" layer="91"/>
<label x="188.96" y="115.72" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="I2C_SDA" class="0">
<segment>
<pinref part="J4" gate="G$1" pin="4"/>
<wire x1="193.57" y1="117.46" x2="189.76" y2="117.46" width="0.1524" layer="91"/>
<label x="188.96" y="118.26" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="LDO_EN" class="0">
<segment>
<pinref part="U2" gate="G$1" pin="EN"/>
<wire x1="133.49" y1="157.46" x2="129.68" y2="157.46" width="0.1524" layer="91"/>
<label x="128.88" y="158.26" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R4" gate="G$1" pin="2"/>
<wire x1="138" y1="150.08" x2="138" y2="153.89" width="0.1524" layer="91"/>
<label x="138" y="154.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J3" gate="G$1" pin="1"/>
<wire x1="118.57" y1="121.27" x2="114.76" y2="121.27" width="0.1524" layer="91"/>
<label x="113.96" y="122.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="LDO_NC" class="0">
<segment>
<pinref part="U2" gate="G$1" pin="NC"/>
<wire x1="166.51" y1="160" x2="170.32" y2="160" width="0.1524" layer="91"/>
<label x="171.12" y="160.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="LED_CHRG_A" class="0">
<segment>
<pinref part="R2" gate="G$1" pin="2"/>
<wire x1="110.08" y1="178" x2="113.89" y2="178" width="0.1524" layer="91"/>
<label x="114.69" y="178.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="D1" gate="G$1" pin="A"/>
<wire x1="121.81" y1="178" x2="125.62" y2="178" width="0.1524" layer="91"/>
<label x="126.42" y="178.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="LED_CHRG_K" class="0">
<segment>
<pinref part="U1" gate="G$1" pin="CHRG"/>
<wire x1="97.78" y1="158.73" x2="101.59" y2="158.73" width="0.1524" layer="91"/>
<label x="102.39" y="159.53" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="D1" gate="G$1" pin="C"/>
<wire x1="114.19" y1="178" x2="110.38" y2="178" width="0.1524" layer="91"/>
<label x="109.58" y="178.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="LED_STDBY_A" class="0">
<segment>
<pinref part="R3" gate="G$1" pin="2"/>
<wire x1="110.08" y1="170" x2="113.89" y2="170" width="0.1524" layer="91"/>
<label x="114.69" y="170.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="D2" gate="G$1" pin="A"/>
<wire x1="121.81" y1="170" x2="125.62" y2="170" width="0.1524" layer="91"/>
<label x="126.42" y="170.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="LED_STDBY_K" class="0">
<segment>
<pinref part="U1" gate="G$1" pin="STDBY"/>
<wire x1="97.78" y1="156.19" x2="101.59" y2="156.19" width="0.1524" layer="91"/>
<label x="102.39" y="156.99" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="D2" gate="G$1" pin="C"/>
<wire x1="114.19" y1="170" x2="110.38" y2="170" width="0.1524" layer="91"/>
<label x="109.58" y="170.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="USB_DM" class="0">
<segment>
<pinref part="J2" gate="G$1" pin="2"/>
<wire x1="13.57" y1="141.27" x2="9.76" y2="141.27" width="0.1524" layer="91"/>
<label x="8.96" y="142.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="USB_DP" class="0">
<segment>
<pinref part="J2" gate="G$1" pin="3"/>
<wire x1="13.57" y1="138.73" x2="9.76" y2="138.73" width="0.1524" layer="91"/>
<label x="8.96" y="139.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="VBAT" class="1">
<segment>
<pinref part="SUPPLY2" gate="G$1" pin="VBAT"/>
<wire x1="45" y1="100" x2="45" y2="96.19" width="0.1524" layer="91"/>
<label x="45" y="96.99" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J1" gate="G$1" pin="1"/>
<wire x1="13.57" y1="176.27" x2="9.76" y2="176.27" width="0.1524" layer="91"/>
<label x="8.96" y="177.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U1" gate="G$1" pin="BAT"/>
<wire x1="97.78" y1="163.81" x2="101.59" y2="163.81" width="0.1524" layer="91"/>
<label x="102.39" y="164.61" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C2" gate="G$1" pin="1"/>
<wire x1="100" y1="145.08" x2="100" y2="148.89" width="0.1524" layer="91"/>
<label x="100" y="149.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U2" gate="G$1" pin="VIN"/>
<wire x1="133.49" y1="162.54" x2="129.68" y2="162.54" width="0.1524" layer="91"/>
<label x="128.88" y="163.34" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R4" gate="G$1" pin="1"/>
<wire x1="138" y1="139.92" x2="138" y2="136.11" width="0.1524" layer="91"/>
<label x="138" y="136.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C3" gate="G$1" pin="1"/>
<wire x1="138" y1="177.08" x2="138" y2="180.89" width="0.1524" layer="91"/>
<label x="138" y="181.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R5" gate="G$1" pin="1"/>
<wire x1="205" y1="169.92" x2="205" y2="166.11" width="0.1524" layer="91"/>
<label x="205" y="166.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J4" gate="G$1" pin="1"/>
<wire x1="193.57" y1="125.08" x2="189.76" y2="125.08" width="0.1524" layer="91"/>
<label x="188.96" y="125.88" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="TP1" gate="G$1" pin="TP"/>
<wire x1="240" y1="175.46" x2="240" y2="171.65" width="0.1524" layer="91"/>
<label x="240" y="172.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="VBAT_SENSE" class="0">
<segment>
<pinref part="R5" gate="G$1" pin="2"/>
<wire x1="205" y1="180.08" x2="205" y2="183.89" width="0.1524" layer="91"/>
<label x="205" y="184.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R6" gate="G$1" pin="1"/>
<wire x1="205" y1="154.92" x2="205" y2="151.11" width="0.1524" layer="91"/>
<label x="205" y="151.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C6" gate="G$1" pin="1"/>
<wire x1="218" y1="165.08" x2="218" y2="168.89" width="0.1524" layer="91"/>
<label x="218" y="169.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="VBUS" class="1">
<segment>
<pinref part="SUPPLY3" gate="G$1" pin="VBUS"/>
<wire x1="60" y1="100" x2="60" y2="96.19" width="0.1524" layer="91"/>
<label x="60" y="96.99" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J2" gate="G$1" pin="1"/>
<wire x1="13.57" y1="143.81" x2="9.76" y2="143.81" width="0.1524" layer="91"/>
<label x="8.96" y="144.61" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U1" gate="G$1" pin="VCC"/>
<wire x1="62.22" y1="163.81" x2="58.41" y2="163.81" width="0.1524" layer="91"/>
<label x="57.61" y="164.61" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U1" gate="G$1" pin="CE"/>
<wire x1="62.22" y1="158.73" x2="58.41" y2="158.73" width="0.1524" layer="91"/>
<label x="57.61" y="159.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="C1" gate="G$1" pin="1"/>
<wire x1="45" y1="150.08" x2="45" y2="153.89" width="0.1524" layer="91"/>
<label x="45" y="154.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R2" gate="G$1" pin="1"/>
<wire x1="99.92" y1="178" x2="96.11" y2="178" width="0.1524" layer="91"/>
<label x="95.31" y="178.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R3" gate="G$1" pin="1"/>
<wire x1="99.92" y1="170" x2="96.11" y2="170" width="0.1524" layer="91"/>
<label x="95.31" y="170.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="TP4" gate="G$1" pin="TP"/>
<wire x1="270" y1="175.46" x2="270" y2="171.65" width="0.1524" layer="91"/>
<label x="270" y="172.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
</nets>
</sheet>
<sheet>
<description>SHEET 2/7 - ESP32-S3 CENTRAL MCU, RESET/BOOT, PROGRAMMING, INDICATORS</description>
<plain>
<wire x1="0" y1="0" x2="380" y2="0" width="0.3" layer="94"/>
<wire x1="380" y1="0" x2="380" y2="260" width="0.3" layer="94"/>
<wire x1="380" y1="260" x2="0" y2="260" width="0.3" layer="94"/>
<wire x1="0" y1="260" x2="0" y2="0" width="0.3" layer="94"/>
<wire x1="0" y1="22" x2="380" y2="22" width="0.3" layer="94"/>
<wire x1="0" y1="10" x2="380" y2="10" width="0.2" layer="94"/>
<text x="3" y="16" size="3" layer="94" ratio="10">SIH26113 - MATERNITY ASSIST BELT - PROTOTYPE CARRIER BOARD</text>
<text x="3" y="12" size="2" layer="94" ratio="10">SHEET 2/7 - ESP32-S3 CENTRAL MCU, RESET/BOOT, PROGRAMMING, INDICATORS</text>
<text x="3" y="5.5" size="1.8" layer="94" ratio="10">NOT A MEDICAL DEVICE. Prototype for engineering evaluation only. Human-connected ECG is NOT isolated - see documentation/README.</text>
<text x="3" y="2" size="1.8" layer="94" ratio="10">4-layer FR-4 1.6 mm (L1 sig / L2 GND plane / L15 3V3 plane / L16 sig) | board 100 x 70 mm | lib SIH26113_Maternity_Assist_Belt.lbr | sheet 2 of 7</text>
<text x="320" y="252" size="3.5" layer="94" ratio="10">SHEET 2/7</text>
<text x="60" y="200" size="2.6" layer="94" ratio="10">SUPPLY DECOUPLING</text>
<text x="120" y="200" size="2.6" layer="94" ratio="10">ESP32-S3-WROOM-1-N8R2</text>
<text x="205" y="200" size="2.6" layer="94" ratio="10">PROGRAMMING / RESET / BOOT</text>
<text x="205" y="120" size="2.6" layer="94" ratio="10">INDICATORS</text>
</plain>
<instances>
<instance part="U3" gate="G$1" x="130" y="120"/>
<instance part="C7" gate="G$1" x="70" y="175"/>
<instance part="C8" gate="G$1" x="58" y="175"/>
<instance part="R7" gate="G$1" x="60" y="150" rot="R90"/>
<instance part="C10" gate="G$1" x="72" y="140"/>
<instance part="SW2" gate="G$1" x="60" y="120"/>
<instance part="R8" gate="G$1" x="88" y="150" rot="R90"/>
<instance part="SW3" gate="G$1" x="88" y="120"/>
<instance part="J5" gate="G$1" x="210" y="150"/>
<instance part="R9" gate="G$1" x="210" y="105"/>
<instance part="D3" gate="G$1" x="224" y="105"/>
<instance part="R10" gate="G$1" x="210" y="96"/>
<instance part="D4" gate="G$1" x="224" y="96"/>
<instance part="TP5" gate="G$1" x="250" y="80"/>
<instance part="TP6" gate="G$1" x="260" y="80"/>
<instance part="SUPPLY5" gate="G$1" x="30" y="60"/>
<instance part="SUPPLY6" gate="G$1" x="45" y="60"/>
</instances>
<busses/>
<nets>
<net name="3V3" class="1">
<segment>
<pinref part="SUPPLY6" gate="G$1" pin="3V3"/>
<wire x1="45" y1="60" x2="45" y2="56.19" width="0.1524" layer="91"/>
<label x="45" y="56.99" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U3" gate="G$1" pin="3V3"/>
<wire x1="108.41" y1="142.86" x2="104.6" y2="142.86" width="0.1524" layer="91"/>
<label x="103.8" y="143.66" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="C7" gate="G$1" pin="1"/>
<wire x1="70" y1="180.08" x2="70" y2="183.89" width="0.1524" layer="91"/>
<label x="70" y="184.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C8" gate="G$1" pin="1"/>
<wire x1="58" y1="180.08" x2="58" y2="183.89" width="0.1524" layer="91"/>
<label x="58" y="184.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R7" gate="G$1" pin="1"/>
<wire x1="60" y1="144.92" x2="60" y2="141.11" width="0.1524" layer="91"/>
<label x="60" y="141.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J5" gate="G$1" pin="2"/>
<wire x1="198.57" y1="153.81" x2="194.76" y2="153.81" width="0.1524" layer="91"/>
<label x="193.96" y="154.61" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R8" gate="G$1" pin="1"/>
<wire x1="88" y1="144.92" x2="88" y2="141.11" width="0.1524" layer="91"/>
<label x="88" y="141.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ANG_SCL" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO42"/>
<wire x1="151.59" y1="112.38" x2="155.4" y2="112.38" width="0.1524" layer="91"/>
<label x="156.2" y="113.18" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ANG_SDA" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO14"/>
<wire x1="108.41" y1="102.22" x2="104.6" y2="102.22" width="0.1524" layer="91"/>
<label x="103.8" y="103.02" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="BUZZER_EN" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO48"/>
<wire x1="151.59" y1="97.14" x2="155.4" y2="97.14" width="0.1524" layer="91"/>
<label x="156.2" y="97.94" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_FR" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO39"/>
<wire x1="151.59" y1="120" x2="155.4" y2="120" width="0.1524" layer="91"/>
<label x="156.2" y="120.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_LOD_N" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO36"/>
<wire x1="151.59" y1="127.62" x2="155.4" y2="127.62" width="0.1524" layer="91"/>
<label x="156.2" y="128.42" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_LOD_P" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO35"/>
<wire x1="151.59" y1="130.16" x2="155.4" y2="130.16" width="0.1524" layer="91"/>
<label x="156.2" y="130.96" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_OUT" class="3">
<segment>
<pinref part="U3" gate="G$1" pin="IO1"/>
<wire x1="108.41" y1="135.24" x2="104.6" y2="135.24" width="0.1524" layer="91"/>
<label x="103.8" y="136.04" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="ECG_SDN" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO37"/>
<wire x1="151.59" y1="125.08" x2="155.4" y2="125.08" width="0.1524" layer="91"/>
<label x="156.2" y="125.88" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ESP_EN" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="EN"/>
<wire x1="108.41" y1="140.32" x2="104.6" y2="140.32" width="0.1524" layer="91"/>
<label x="103.8" y="141.12" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R7" gate="G$1" pin="2"/>
<wire x1="60" y1="155.08" x2="60" y2="158.89" width="0.1524" layer="91"/>
<label x="60" y="159.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C10" gate="G$1" pin="1"/>
<wire x1="72" y1="145.08" x2="72" y2="148.89" width="0.1524" layer="91"/>
<label x="72" y="149.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="SW2" gate="G$1" pin="P"/>
<wire x1="54.92" y1="120" x2="51.11" y2="120" width="0.1524" layer="91"/>
<label x="50.31" y="120.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="J5" gate="G$1" pin="5"/>
<wire x1="198.57" y1="146.19" x2="194.76" y2="146.19" width="0.1524" layer="91"/>
<label x="193.96" y="146.99" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="ESP_IO0" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO0"/>
<wire x1="108.41" y1="137.78" x2="104.6" y2="137.78" width="0.1524" layer="91"/>
<label x="103.8" y="138.58" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R8" gate="G$1" pin="2"/>
<wire x1="88" y1="155.08" x2="88" y2="158.89" width="0.1524" layer="91"/>
<label x="88" y="159.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="SW3" gate="G$1" pin="P"/>
<wire x1="82.92" y1="120" x2="79.11" y2="120" width="0.1524" layer="91"/>
<label x="78.31" y="120.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="J5" gate="G$1" pin="6"/>
<wire x1="198.57" y1="143.65" x2="194.76" y2="143.65" width="0.1524" layer="91"/>
<label x="193.96" y="144.45" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="FSR1_ADC" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO4"/>
<wire x1="108.41" y1="127.62" x2="104.6" y2="127.62" width="0.1524" layer="91"/>
<label x="103.8" y="128.42" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="FSR2_ADC" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO5"/>
<wire x1="108.41" y1="125.08" x2="104.6" y2="125.08" width="0.1524" layer="91"/>
<label x="103.8" y="125.88" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="FSR3_ADC" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO6"/>
<wire x1="108.41" y1="122.54" x2="104.6" y2="122.54" width="0.1524" layer="91"/>
<label x="103.8" y="123.34" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="FSR4_ADC" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO7"/>
<wire x1="108.41" y1="120" x2="104.6" y2="120" width="0.1524" layer="91"/>
<label x="103.8" y="120.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="GND" class="1">
<segment>
<pinref part="SUPPLY5" gate="G$1" pin="GND"/>
<wire x1="30" y1="62.54" x2="30" y2="66.35" width="0.1524" layer="91"/>
<label x="30" y="67.15" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U3" gate="G$1" pin="GND@1"/>
<wire x1="108.41" y1="145.4" x2="104.6" y2="145.4" width="0.1524" layer="91"/>
<label x="103.8" y="146.2" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U3" gate="G$1" pin="GND@40"/>
<wire x1="151.59" y1="145.4" x2="155.4" y2="145.4" width="0.1524" layer="91"/>
<label x="156.2" y="146.2" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U3" gate="G$1" pin="EPAD"/>
<wire x1="151.59" y1="142.86" x2="155.4" y2="142.86" width="0.1524" layer="91"/>
<label x="156.2" y="143.66" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C7" gate="G$1" pin="2"/>
<wire x1="70" y1="169.92" x2="70" y2="166.11" width="0.1524" layer="91"/>
<label x="70" y="166.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C8" gate="G$1" pin="2"/>
<wire x1="58" y1="169.92" x2="58" y2="166.11" width="0.1524" layer="91"/>
<label x="58" y="166.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C10" gate="G$1" pin="2"/>
<wire x1="72" y1="134.92" x2="72" y2="131.11" width="0.1524" layer="91"/>
<label x="72" y="131.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="SW2" gate="G$1" pin="N"/>
<wire x1="65.08" y1="120" x2="68.89" y2="120" width="0.1524" layer="91"/>
<label x="69.69" y="120.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="SW3" gate="G$1" pin="N"/>
<wire x1="93.08" y1="120" x2="96.89" y2="120" width="0.1524" layer="91"/>
<label x="97.69" y="120.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J5" gate="G$1" pin="1"/>
<wire x1="198.57" y1="156.35" x2="194.76" y2="156.35" width="0.1524" layer="91"/>
<label x="193.96" y="157.15" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="D3" gate="G$1" pin="C"/>
<wire x1="220.19" y1="105" x2="216.38" y2="105" width="0.1524" layer="91"/>
<label x="215.58" y="105.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="D4" gate="G$1" pin="C"/>
<wire x1="220.19" y1="96" x2="216.38" y2="96" width="0.1524" layer="91"/>
<label x="215.58" y="96.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="HALL_LIMIT" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO41"/>
<wire x1="151.59" y1="114.92" x2="155.4" y2="114.92" width="0.1524" layer="91"/>
<label x="156.2" y="115.72" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="HX_DOUT" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO21"/>
<wire x1="151.59" y1="132.7" x2="155.4" y2="132.7" width="0.1524" layer="91"/>
<label x="156.2" y="133.5" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="HX_SCK" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO38"/>
<wire x1="151.59" y1="122.54" x2="155.4" y2="122.54" width="0.1524" layer="91"/>
<label x="156.2" y="123.34" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="I2C_SCL" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO16"/>
<wire x1="108.41" y1="97.14" x2="104.6" y2="97.14" width="0.1524" layer="91"/>
<label x="103.8" y="97.94" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="I2C_SDA" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO15"/>
<wire x1="108.41" y1="99.68" x2="104.6" y2="99.68" width="0.1524" layer="91"/>
<label x="103.8" y="100.48" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="IMU_INT1" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO17"/>
<wire x1="108.41" y1="94.6" x2="104.6" y2="94.6" width="0.1524" layer="91"/>
<label x="103.8" y="95.4" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="IMU_INT2" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO18"/>
<wire x1="151.59" y1="140.32" x2="155.4" y2="140.32" width="0.1524" layer="91"/>
<label x="156.2" y="141.12" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="IO3_SPARE" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO3"/>
<wire x1="108.41" y1="130.16" x2="104.6" y2="130.16" width="0.1524" layer="91"/>
<label x="103.8" y="130.96" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="TP5" gate="G$1" pin="TP"/>
<wire x1="250" y1="77.46" x2="250" y2="73.65" width="0.1524" layer="91"/>
<label x="250" y="74.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="LED_ALERT" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO46"/>
<wire x1="151.59" y1="102.22" x2="155.4" y2="102.22" width="0.1524" layer="91"/>
<label x="156.2" y="103.02" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R10" gate="G$1" pin="1"/>
<wire x1="204.92" y1="96" x2="201.11" y2="96" width="0.1524" layer="91"/>
<label x="200.31" y="96.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="LED_ALERT_A" class="0">
<segment>
<pinref part="R10" gate="G$1" pin="2"/>
<wire x1="215.08" y1="96" x2="218.89" y2="96" width="0.1524" layer="91"/>
<label x="219.69" y="96.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="D4" gate="G$1" pin="A"/>
<wire x1="227.81" y1="96" x2="231.62" y2="96" width="0.1524" layer="91"/>
<label x="232.42" y="96.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="LED_STATUS" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO45"/>
<wire x1="151.59" y1="104.76" x2="155.4" y2="104.76" width="0.1524" layer="91"/>
<label x="156.2" y="105.56" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R9" gate="G$1" pin="1"/>
<wire x1="204.92" y1="105" x2="201.11" y2="105" width="0.1524" layer="91"/>
<label x="200.31" y="105.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="LED_STATUS_A" class="0">
<segment>
<pinref part="R9" gate="G$1" pin="2"/>
<wire x1="215.08" y1="105" x2="218.89" y2="105" width="0.1524" layer="91"/>
<label x="219.69" y="105.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="D3" gate="G$1" pin="A"/>
<wire x1="227.81" y1="105" x2="231.62" y2="105" width="0.1524" layer="91"/>
<label x="232.42" y="105.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="MOTOR_EN" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO47"/>
<wire x1="151.59" y1="99.68" x2="155.4" y2="99.68" width="0.1524" layer="91"/>
<label x="156.2" y="100.48" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="PIEZO_ADC" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO2"/>
<wire x1="108.41" y1="132.7" x2="104.6" y2="132.7" width="0.1524" layer="91"/>
<label x="103.8" y="133.5" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="SD_CS" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO10"/>
<wire x1="108.41" y1="112.38" x2="104.6" y2="112.38" width="0.1524" layer="91"/>
<label x="103.8" y="113.18" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="SD_MISO" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO13"/>
<wire x1="108.41" y1="104.76" x2="104.6" y2="104.76" width="0.1524" layer="91"/>
<label x="103.8" y="105.56" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="SD_MOSI" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO11"/>
<wire x1="108.41" y1="109.84" x2="104.6" y2="109.84" width="0.1524" layer="91"/>
<label x="103.8" y="110.64" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="SD_SCK" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO12"/>
<wire x1="108.41" y1="107.3" x2="104.6" y2="107.3" width="0.1524" layer="91"/>
<label x="103.8" y="108.1" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="SOS_GPIO" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO40"/>
<wire x1="151.59" y1="117.46" x2="155.4" y2="117.46" width="0.1524" layer="91"/>
<label x="156.2" y="118.26" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="STRETCH_ADC" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO8"/>
<wire x1="108.41" y1="117.46" x2="104.6" y2="117.46" width="0.1524" layer="91"/>
<label x="103.8" y="118.26" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="TMP_ALERT" class="0">
<segment>
<pinref part="TP6" gate="G$1" pin="TP"/>
<wire x1="260" y1="77.46" x2="260" y2="73.65" width="0.1524" layer="91"/>
<label x="260" y="74.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="UART_RX" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="RXD0"/>
<wire x1="151.59" y1="107.3" x2="155.4" y2="107.3" width="0.1524" layer="91"/>
<label x="156.2" y="108.1" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J5" gate="G$1" pin="4"/>
<wire x1="198.57" y1="148.73" x2="194.76" y2="148.73" width="0.1524" layer="91"/>
<label x="193.96" y="149.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="UART_TX" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="TXD0"/>
<wire x1="151.59" y1="109.84" x2="155.4" y2="109.84" width="0.1524" layer="91"/>
<label x="156.2" y="110.64" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J5" gate="G$1" pin="3"/>
<wire x1="198.57" y1="151.27" x2="194.76" y2="151.27" width="0.1524" layer="91"/>
<label x="193.96" y="152.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="USB_DM" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO19"/>
<wire x1="151.59" y1="137.78" x2="155.4" y2="137.78" width="0.1524" layer="91"/>
<label x="156.2" y="138.58" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="USB_DP" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO20"/>
<wire x1="151.59" y1="135.24" x2="155.4" y2="135.24" width="0.1524" layer="91"/>
<label x="156.2" y="136.04" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="VBAT_SENSE" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="IO9"/>
<wire x1="108.41" y1="114.92" x2="104.6" y2="114.92" width="0.1524" layer="91"/>
<label x="103.8" y="115.72" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
</nets>
</sheet>
<sheet>
<description>SHEET 3/7 - I2C SENSORS (TMP117, LSM6DSOX, AS5600) - TWO BUSSES</description>
<plain>
<wire x1="0" y1="0" x2="380" y2="0" width="0.3" layer="94"/>
<wire x1="380" y1="0" x2="380" y2="260" width="0.3" layer="94"/>
<wire x1="380" y1="260" x2="0" y2="260" width="0.3" layer="94"/>
<wire x1="0" y1="260" x2="0" y2="0" width="0.3" layer="94"/>
<wire x1="0" y1="22" x2="380" y2="22" width="0.3" layer="94"/>
<wire x1="0" y1="10" x2="380" y2="10" width="0.2" layer="94"/>
<text x="3" y="16" size="3" layer="94" ratio="10">SIH26113 - MATERNITY ASSIST BELT - PROTOTYPE CARRIER BOARD</text>
<text x="3" y="12" size="2" layer="94" ratio="10">SHEET 3/7 - I2C SENSORS (TMP117, LSM6DSOX, AS5600) - TWO BUSSES</text>
<text x="3" y="5.5" size="1.8" layer="94" ratio="10">NOT A MEDICAL DEVICE. Prototype for engineering evaluation only. Human-connected ECG is NOT isolated - see documentation/README.</text>
<text x="3" y="2" size="1.8" layer="94" ratio="10">4-layer FR-4 1.6 mm (L1 sig / L2 GND plane / L15 3V3 plane / L16 sig) | board 100 x 70 mm | lib SIH26113_Maternity_Assist_Belt.lbr | sheet 3 of 7</text>
<text x="320" y="252" size="3.5" layer="94" ratio="10">SHEET 3/7</text>
<text x="40" y="200" size="2.6" layer="94" ratio="10">SENSOR BUS I2C0 PULL-UPS</text>
<text x="100" y="200" size="2.6" layer="94" ratio="10">TMP117 / LSM6DSOX</text>
<text x="40" y="110" size="2.6" layer="94" ratio="10">ANGLE BUS I2C1 PULL-UPS</text>
<text x="100" y="110" size="2.6" layer="94" ratio="10">AS5600 + SIDE-B</text>
</plain>
<instances>
<instance part="R11" gate="G$1" x="40" y="175" rot="R90"/>
<instance part="R12" gate="G$1" x="52" y="175" rot="R90"/>
<instance part="U4" gate="G$1" x="100" y="175"/>
<instance part="C11" gate="G$1" x="82" y="165"/>
<instance part="R13" gate="G$1" x="130" y="190" rot="R90"/>
<instance part="U5" gate="G$1" x="100" y="130"/>
<instance part="C12" gate="G$1" x="78" y="120"/>
<instance part="C13" gate="G$1" x="68" y="120"/>
<instance part="TP7" gate="G$1" x="140" y="118"/>
<instance part="R15" gate="G$1" x="40" y="90" rot="R90"/>
<instance part="R16" gate="G$1" x="52" y="90" rot="R90"/>
<instance part="U6" gate="G$1" x="100" y="80"/>
<instance part="C14" gate="G$1" x="78" y="70"/>
<instance part="C15" gate="G$1" x="68" y="70"/>
<instance part="TP8" gate="G$1" x="140" y="68"/>
<instance part="TP9" gate="G$1" x="150" y="68"/>
<instance part="J6" gate="G$1" x="200" y="80"/>
<instance part="R17" gate="G$1" x="230" y="90"/>
<instance part="SUPPLY7" gate="G$1" x="30" y="40"/>
<instance part="SUPPLY8" gate="G$1" x="45" y="40"/>
</instances>
<busses/>
<nets>
<net name="3V3" class="1">
<segment>
<pinref part="SUPPLY8" gate="G$1" pin="3V3"/>
<wire x1="45" y1="40" x2="45" y2="36.19" width="0.1524" layer="91"/>
<label x="45" y="36.99" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R11" gate="G$1" pin="1"/>
<wire x1="40" y1="169.92" x2="40" y2="166.11" width="0.1524" layer="91"/>
<label x="40" y="166.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R12" gate="G$1" pin="1"/>
<wire x1="52" y1="169.92" x2="52" y2="166.11" width="0.1524" layer="91"/>
<label x="52" y="166.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U4" gate="G$1" pin="V+"/>
<wire x1="83.49" y1="178.81" x2="79.68" y2="178.81" width="0.1524" layer="91"/>
<label x="78.88" y="179.61" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="C11" gate="G$1" pin="1"/>
<wire x1="82" y1="170.08" x2="82" y2="173.89" width="0.1524" layer="91"/>
<label x="82" y="174.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R13" gate="G$1" pin="1"/>
<wire x1="130" y1="184.92" x2="130" y2="181.11" width="0.1524" layer="91"/>
<label x="130" y="181.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U5" gate="G$1" pin="VDD"/>
<wire x1="82.22" y1="138.89" x2="78.41" y2="138.89" width="0.1524" layer="91"/>
<label x="77.61" y="139.69" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U5" gate="G$1" pin="VDDIO"/>
<wire x1="82.22" y1="136.35" x2="78.41" y2="136.35" width="0.1524" layer="91"/>
<label x="77.61" y="137.15" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U5" gate="G$1" pin="CS"/>
<wire x1="82.22" y1="128.73" x2="78.41" y2="128.73" width="0.1524" layer="91"/>
<label x="77.61" y="129.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U5" gate="G$1" pin="SDO_AUX"/>
<wire x1="117.78" y1="121.11" x2="121.59" y2="121.11" width="0.1524" layer="91"/>
<label x="122.39" y="121.91" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C12" gate="G$1" pin="1"/>
<wire x1="78" y1="125.08" x2="78" y2="128.89" width="0.1524" layer="91"/>
<label x="78" y="129.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C13" gate="G$1" pin="1"/>
<wire x1="68" y1="125.08" x2="68" y2="128.89" width="0.1524" layer="91"/>
<label x="68" y="129.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R15" gate="G$1" pin="1"/>
<wire x1="40" y1="84.92" x2="40" y2="81.11" width="0.1524" layer="91"/>
<label x="40" y="81.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R16" gate="G$1" pin="1"/>
<wire x1="52" y1="84.92" x2="52" y2="81.11" width="0.1524" layer="91"/>
<label x="52" y="81.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U6" gate="G$1" pin="VDD5V"/>
<wire x1="82.22" y1="83.81" x2="78.41" y2="83.81" width="0.1524" layer="91"/>
<label x="77.61" y="84.61" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U6" gate="G$1" pin="VDD3V3"/>
<wire x1="82.22" y1="81.27" x2="78.41" y2="81.27" width="0.1524" layer="91"/>
<label x="77.61" y="82.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="C14" gate="G$1" pin="1"/>
<wire x1="78" y1="75.08" x2="78" y2="78.89" width="0.1524" layer="91"/>
<label x="78" y="79.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C15" gate="G$1" pin="1"/>
<wire x1="68" y1="75.08" x2="68" y2="78.89" width="0.1524" layer="91"/>
<label x="68" y="79.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J6" gate="G$1" pin="1"/>
<wire x1="188.57" y1="85.08" x2="184.76" y2="85.08" width="0.1524" layer="91"/>
<label x="183.96" y="85.88" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="ANG2_OUT" class="0">
<segment>
<pinref part="J6" gate="G$1" pin="5"/>
<wire x1="188.57" y1="74.92" x2="184.76" y2="74.92" width="0.1524" layer="91"/>
<label x="183.96" y="75.72" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R17" gate="G$1" pin="1"/>
<wire x1="224.92" y1="90" x2="221.11" y2="90" width="0.1524" layer="91"/>
<label x="220.31" y="90.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="ANG_SCL" class="0">
<segment>
<pinref part="R16" gate="G$1" pin="2"/>
<wire x1="52" y1="95.08" x2="52" y2="98.89" width="0.1524" layer="91"/>
<label x="52" y="99.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U6" gate="G$1" pin="SCL"/>
<wire x1="117.78" y1="81.27" x2="121.59" y2="81.27" width="0.1524" layer="91"/>
<label x="122.39" y="82.07" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J6" gate="G$1" pin="4"/>
<wire x1="188.57" y1="77.46" x2="184.76" y2="77.46" width="0.1524" layer="91"/>
<label x="183.96" y="78.26" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="ANG_SDA" class="0">
<segment>
<pinref part="R15" gate="G$1" pin="2"/>
<wire x1="40" y1="95.08" x2="40" y2="98.89" width="0.1524" layer="91"/>
<label x="40" y="99.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U6" gate="G$1" pin="SDA"/>
<wire x1="117.78" y1="83.81" x2="121.59" y2="83.81" width="0.1524" layer="91"/>
<label x="122.39" y="84.61" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J6" gate="G$1" pin="3"/>
<wire x1="188.57" y1="80" x2="184.76" y2="80" width="0.1524" layer="91"/>
<label x="183.96" y="80.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="AS_OUT" class="0">
<segment>
<pinref part="U6" gate="G$1" pin="OUT"/>
<wire x1="117.78" y1="78.73" x2="121.59" y2="78.73" width="0.1524" layer="91"/>
<label x="122.39" y="79.53" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="TP8" gate="G$1" pin="TP"/>
<wire x1="140" y1="65.46" x2="140" y2="61.65" width="0.1524" layer="91"/>
<label x="140" y="62.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="AS_PGO" class="0">
<segment>
<pinref part="U6" gate="G$1" pin="PGO"/>
<wire x1="117.78" y1="76.19" x2="121.59" y2="76.19" width="0.1524" layer="91"/>
<label x="122.39" y="76.99" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="TP9" gate="G$1" pin="TP"/>
<wire x1="150" y1="65.46" x2="150" y2="61.65" width="0.1524" layer="91"/>
<label x="150" y="62.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="GND" class="1">
<segment>
<pinref part="SUPPLY7" gate="G$1" pin="GND"/>
<wire x1="30" y1="42.54" x2="30" y2="46.35" width="0.1524" layer="91"/>
<label x="30" y="47.15" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U4" gate="G$1" pin="GND"/>
<wire x1="83.49" y1="176.27" x2="79.68" y2="176.27" width="0.1524" layer="91"/>
<label x="78.88" y="177.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U4" gate="G$1" pin="TPAD"/>
<wire x1="116.51" y1="171.19" x2="120.32" y2="171.19" width="0.1524" layer="91"/>
<label x="121.12" y="171.99" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C11" gate="G$1" pin="2"/>
<wire x1="82" y1="159.92" x2="82" y2="156.11" width="0.1524" layer="91"/>
<label x="82" y="156.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U5" gate="G$1" pin="GND@6"/>
<wire x1="82.22" y1="133.81" x2="78.41" y2="133.81" width="0.1524" layer="91"/>
<label x="77.61" y="134.61" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U5" gate="G$1" pin="GND@7"/>
<wire x1="82.22" y1="131.27" x2="78.41" y2="131.27" width="0.1524" layer="91"/>
<label x="77.61" y="132.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U5" gate="G$1" pin="SDO/SA0"/>
<wire x1="82.22" y1="126.19" x2="78.41" y2="126.19" width="0.1524" layer="91"/>
<label x="77.61" y="126.99" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U5" gate="G$1" pin="SDx"/>
<wire x1="117.78" y1="128.73" x2="121.59" y2="128.73" width="0.1524" layer="91"/>
<label x="122.39" y="129.53" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U5" gate="G$1" pin="SCx"/>
<wire x1="117.78" y1="126.19" x2="121.59" y2="126.19" width="0.1524" layer="91"/>
<label x="122.39" y="126.99" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C12" gate="G$1" pin="2"/>
<wire x1="78" y1="114.92" x2="78" y2="111.11" width="0.1524" layer="91"/>
<label x="78" y="111.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C13" gate="G$1" pin="2"/>
<wire x1="68" y1="114.92" x2="68" y2="111.11" width="0.1524" layer="91"/>
<label x="68" y="111.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U6" gate="G$1" pin="GND"/>
<wire x1="82.22" y1="78.73" x2="78.41" y2="78.73" width="0.1524" layer="91"/>
<label x="77.61" y="79.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U6" gate="G$1" pin="DIR"/>
<wire x1="82.22" y1="76.19" x2="78.41" y2="76.19" width="0.1524" layer="91"/>
<label x="77.61" y="76.99" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="C14" gate="G$1" pin="2"/>
<wire x1="78" y1="64.92" x2="78" y2="61.11" width="0.1524" layer="91"/>
<label x="78" y="61.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C15" gate="G$1" pin="2"/>
<wire x1="68" y1="64.92" x2="68" y2="61.11" width="0.1524" layer="91"/>
<label x="68" y="61.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J6" gate="G$1" pin="2"/>
<wire x1="188.57" y1="82.54" x2="184.76" y2="82.54" width="0.1524" layer="91"/>
<label x="183.96" y="83.34" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U4" gate="G$1" pin="ADD0"/>
<wire x1="83.49" y1="173.73" x2="79.68" y2="173.73" width="0.1524" layer="91"/>
<label x="78.88" y="174.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="I2C_SCL" class="0">
<segment>
<pinref part="R12" gate="G$1" pin="2"/>
<wire x1="52" y1="180.08" x2="52" y2="183.89" width="0.1524" layer="91"/>
<label x="52" y="184.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U4" gate="G$1" pin="SCL"/>
<wire x1="116.51" y1="176.27" x2="120.32" y2="176.27" width="0.1524" layer="91"/>
<label x="121.12" y="177.07" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U5" gate="G$1" pin="SCL"/>
<wire x1="117.78" y1="136.35" x2="121.59" y2="136.35" width="0.1524" layer="91"/>
<label x="122.39" y="137.15" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="I2C_SDA" class="0">
<segment>
<pinref part="R11" gate="G$1" pin="2"/>
<wire x1="40" y1="180.08" x2="40" y2="183.89" width="0.1524" layer="91"/>
<label x="40" y="184.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U4" gate="G$1" pin="SDA"/>
<wire x1="116.51" y1="178.81" x2="120.32" y2="178.81" width="0.1524" layer="91"/>
<label x="121.12" y="179.61" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U5" gate="G$1" pin="SDA"/>
<wire x1="117.78" y1="138.89" x2="121.59" y2="138.89" width="0.1524" layer="91"/>
<label x="122.39" y="139.69" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="IMU_INT1" class="0">
<segment>
<pinref part="U5" gate="G$1" pin="INT1"/>
<wire x1="117.78" y1="133.81" x2="121.59" y2="133.81" width="0.1524" layer="91"/>
<label x="122.39" y="134.61" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="TP7" gate="G$1" pin="TP"/>
<wire x1="140" y1="115.46" x2="140" y2="111.65" width="0.1524" layer="91"/>
<label x="140" y="112.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="IMU_INT2" class="0">
<segment>
<pinref part="U5" gate="G$1" pin="INT2"/>
<wire x1="117.78" y1="131.27" x2="121.59" y2="131.27" width="0.1524" layer="91"/>
<label x="122.39" y="132.07" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="IMU_OCS_AUX" class="0">
<segment>
<pinref part="U5" gate="G$1" pin="OCS_AUX"/>
<wire x1="117.78" y1="123.65" x2="121.59" y2="123.65" width="0.1524" layer="91"/>
<label x="122.39" y="124.45" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="IO3_SPARE" class="0">
<segment>
<pinref part="R17" gate="G$1" pin="2"/>
<wire x1="235.08" y1="90" x2="238.89" y2="90" width="0.1524" layer="91"/>
<label x="239.69" y="90.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="TMP_ALERT" class="0">
<segment>
<pinref part="U4" gate="G$1" pin="ALERT"/>
<wire x1="116.51" y1="173.73" x2="120.32" y2="173.73" width="0.1524" layer="91"/>
<label x="121.12" y="174.53" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R13" gate="G$1" pin="2"/>
<wire x1="130" y1="195.08" x2="130" y2="198.89" width="0.1524" layer="91"/>
<label x="130" y="199.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
</nets>
</sheet>
<sheet>
<description>SHEET 4/7 - ECG ANALOG FRONT END (AD8232)</description>
<plain>
<wire x1="0" y1="0" x2="380" y2="0" width="0.3" layer="94"/>
<wire x1="380" y1="0" x2="380" y2="260" width="0.3" layer="94"/>
<wire x1="380" y1="260" x2="0" y2="260" width="0.3" layer="94"/>
<wire x1="0" y1="260" x2="0" y2="0" width="0.3" layer="94"/>
<wire x1="0" y1="22" x2="380" y2="22" width="0.3" layer="94"/>
<wire x1="0" y1="10" x2="380" y2="10" width="0.2" layer="94"/>
<text x="3" y="16" size="3" layer="94" ratio="10">SIH26113 - MATERNITY ASSIST BELT - PROTOTYPE CARRIER BOARD</text>
<text x="3" y="12" size="2" layer="94" ratio="10">SHEET 4/7 - ECG ANALOG FRONT END (AD8232)</text>
<text x="3" y="5.5" size="1.8" layer="94" ratio="10">NOT A MEDICAL DEVICE. Prototype for engineering evaluation only. Human-connected ECG is NOT isolated - see documentation/README.</text>
<text x="3" y="2" size="1.8" layer="94" ratio="10">4-layer FR-4 1.6 mm (L1 sig / L2 GND plane / L15 3V3 plane / L16 sig) | board 100 x 70 mm | lib SIH26113_Maternity_Assist_Belt.lbr | sheet 4 of 7</text>
<text x="320" y="252" size="3.5" layer="94" ratio="10">SHEET 4/7</text>
<text x="30" y="200" size="2.6" layer="94" ratio="10">ELECTRODE INTERFACE + PROTECTION</text>
<text x="150" y="200" size="2.6" layer="94" ratio="10">AD8232 (Vs = 3V3 ONLY)</text>
<text x="200" y="200" size="2.6" layer="94" ratio="10">2-POLE HPF</text>
<text x="255" y="200" size="2.6" layer="94" ratio="10">2-POLE LPF, GAIN 11</text>
</plain>
<instances>
<instance part="U7" gate="G$1" x="150" y="130"/>
<instance part="J7" gate="G$1" x="30" y="165"/>
<instance part="R18" gate="G$1" x="60" y="172"/>
<instance part="R19" gate="G$1" x="60" y="164"/>
<instance part="R20" gate="G$1" x="60" y="150"/>
<instance part="R21" gate="G$1" x="80" y="185" rot="R90"/>
<instance part="R22" gate="G$1" x="92" y="185" rot="R90"/>
<instance part="R23" gate="G$1" x="112" y="100" rot="R90"/>
<instance part="R24" gate="G$1" x="112" y="85" rot="R90"/>
<instance part="C16" gate="G$1" x="124" y="85"/>
<instance part="C17" gate="G$1" x="90" y="140"/>
<instance part="C18" gate="G$1" x="190" y="175"/>
<instance part="R25" gate="G$1" x="205" y="185"/>
<instance part="C19" gate="G$1" x="220" y="175"/>
<instance part="R26" gate="G$1" x="235" y="165" rot="R90"/>
<instance part="R27" gate="G$1" x="250" y="150"/>
<instance part="C20" gate="G$1" x="262" y="140"/>
<instance part="R28" gate="G$1" x="250" y="120"/>
<instance part="R29" gate="G$1" x="250" y="112"/>
<instance part="C21" gate="G$1" x="262" y="104"/>
<instance part="R30" gate="G$1" x="280" y="130"/>
<instance part="C22" gate="G$1" x="292" y="120"/>
<instance part="R31" gate="G$1" x="120" y="160" rot="R90"/>
<instance part="R32" gate="G$1" x="120" y="140" rot="R90"/>
<instance part="C23" gate="G$1" x="140" y="190"/>
<instance part="C24" gate="G$1" x="152" y="190"/>
<instance part="TP10" gate="G$1" x="305" y="130"/>
<instance part="TP11" gate="G$1" x="305" y="120"/>
<instance part="SUPPLY9" gate="G$1" x="30" y="60"/>
<instance part="SUPPLY10" gate="G$1" x="45" y="60"/>
</instances>
<busses/>
<nets>
<net name="3V3" class="1">
<segment>
<pinref part="SUPPLY10" gate="G$1" pin="3V3"/>
<wire x1="45" y1="60" x2="45" y2="56.19" width="0.1524" layer="91"/>
<label x="45" y="56.99" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U7" gate="G$1" pin="+VS"/>
<wire x1="129.68" y1="142.7" x2="125.87" y2="142.7" width="0.1524" layer="91"/>
<label x="125.07" y="143.5" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R21" gate="G$1" pin="1"/>
<wire x1="80" y1="179.92" x2="80" y2="176.11" width="0.1524" layer="91"/>
<label x="80" y="176.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R22" gate="G$1" pin="1"/>
<wire x1="92" y1="179.92" x2="92" y2="176.11" width="0.1524" layer="91"/>
<label x="92" y="176.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R23" gate="G$1" pin="1"/>
<wire x1="112" y1="94.92" x2="112" y2="91.11" width="0.1524" layer="91"/>
<label x="112" y="91.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R31" gate="G$1" pin="1"/>
<wire x1="120" y1="154.92" x2="120" y2="151.11" width="0.1524" layer="91"/>
<label x="120" y="151.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C23" gate="G$1" pin="1"/>
<wire x1="140" y1="195.08" x2="140" y2="198.89" width="0.1524" layer="91"/>
<label x="140" y="199.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C24" gate="G$1" pin="1"/>
<wire x1="152" y1="195.08" x2="152" y2="198.89" width="0.1524" layer="91"/>
<label x="152" y="199.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_FR" class="0">
<segment>
<pinref part="U7" gate="G$1" pin="FR"/>
<wire x1="129.68" y1="117.3" x2="125.87" y2="117.3" width="0.1524" layer="91"/>
<label x="125.07" y="118.1" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R32" gate="G$1" pin="1"/>
<wire x1="120" y1="134.92" x2="120" y2="131.11" width="0.1524" layer="91"/>
<label x="120" y="131.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_HPDRIVE" class="0">
<segment>
<pinref part="U7" gate="G$1" pin="HPDRIVE"/>
<wire x1="170.32" y1="137.62" x2="174.13" y2="137.62" width="0.1524" layer="91"/>
<label x="174.93" y="138.42" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C18" gate="G$1" pin="1"/>
<wire x1="190" y1="180.08" x2="190" y2="183.89" width="0.1524" layer="91"/>
<label x="190" y="184.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_HPSENSE" class="3">
<segment>
<pinref part="U7" gate="G$1" pin="HPSENSE"/>
<wire x1="170.32" y1="140.16" x2="174.13" y2="140.16" width="0.1524" layer="91"/>
<label x="174.93" y="140.96" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C18" gate="G$1" pin="2"/>
<wire x1="190" y1="169.92" x2="190" y2="166.11" width="0.1524" layer="91"/>
<label x="190" y="166.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R25" gate="G$1" pin="1"/>
<wire x1="199.92" y1="185" x2="196.11" y2="185" width="0.1524" layer="91"/>
<label x="195.31" y="185.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="ECG_IAOUT" class="3">
<segment>
<pinref part="U7" gate="G$1" pin="IAOUT"/>
<wire x1="170.32" y1="142.7" x2="174.13" y2="142.7" width="0.1524" layer="91"/>
<label x="174.93" y="143.5" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R25" gate="G$1" pin="2"/>
<wire x1="210.08" y1="185" x2="213.89" y2="185" width="0.1524" layer="91"/>
<label x="214.69" y="185.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C19" gate="G$1" pin="1"/>
<wire x1="220" y1="180.08" x2="220" y2="183.89" width="0.1524" layer="91"/>
<label x="220" y="184.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_LA" class="3">
<segment>
<pinref part="J7" gate="G$1" pin="1"/>
<wire x1="18.57" y1="167.54" x2="14.76" y2="167.54" width="0.1524" layer="91"/>
<label x="13.96" y="168.34" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R18" gate="G$1" pin="1"/>
<wire x1="54.92" y1="172" x2="51.11" y2="172" width="0.1524" layer="91"/>
<label x="50.31" y="172.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="ECG_LA_F" class="3">
<segment>
<pinref part="R18" gate="G$1" pin="2"/>
<wire x1="65.08" y1="172" x2="68.89" y2="172" width="0.1524" layer="91"/>
<label x="69.69" y="172.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U7" gate="G$1" pin="+IN"/>
<wire x1="129.68" y1="137.62" x2="125.87" y2="137.62" width="0.1524" layer="91"/>
<label x="125.07" y="138.42" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R21" gate="G$1" pin="2"/>
<wire x1="80" y1="190.08" x2="80" y2="193.89" width="0.1524" layer="91"/>
<label x="80" y="194.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_LOD_N" class="0">
<segment>
<pinref part="U7" gate="G$1" pin="LOD-"/>
<wire x1="170.32" y1="122.38" x2="174.13" y2="122.38" width="0.1524" layer="91"/>
<label x="174.93" y="123.18" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_LOD_P" class="0">
<segment>
<pinref part="U7" gate="G$1" pin="LOD+"/>
<wire x1="170.32" y1="124.92" x2="174.13" y2="124.92" width="0.1524" layer="91"/>
<label x="174.93" y="125.72" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_OPM" class="3">
<segment>
<pinref part="U7" gate="G$1" pin="OPAMP-"/>
<wire x1="170.32" y1="130" x2="174.13" y2="130" width="0.1524" layer="91"/>
<label x="174.93" y="130.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R28" gate="G$1" pin="1"/>
<wire x1="244.92" y1="120" x2="241.11" y2="120" width="0.1524" layer="91"/>
<label x="240.31" y="120.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R29" gate="G$1" pin="1"/>
<wire x1="244.92" y1="112" x2="241.11" y2="112" width="0.1524" layer="91"/>
<label x="240.31" y="112.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="C21" gate="G$1" pin="1"/>
<wire x1="262" y1="109.08" x2="262" y2="112.89" width="0.1524" layer="91"/>
<label x="262" y="113.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_OPP" class="3">
<segment>
<pinref part="U7" gate="G$1" pin="OPAMP+"/>
<wire x1="170.32" y1="132.54" x2="174.13" y2="132.54" width="0.1524" layer="91"/>
<label x="174.93" y="133.34" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R27" gate="G$1" pin="2"/>
<wire x1="255.08" y1="150" x2="258.89" y2="150" width="0.1524" layer="91"/>
<label x="259.69" y="150.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C20" gate="G$1" pin="1"/>
<wire x1="262" y1="145.08" x2="262" y2="148.89" width="0.1524" layer="91"/>
<label x="262" y="149.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_OUT" class="3">
<segment>
<pinref part="R30" gate="G$1" pin="2"/>
<wire x1="285.08" y1="130" x2="288.89" y2="130" width="0.1524" layer="91"/>
<label x="289.69" y="130.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C22" gate="G$1" pin="1"/>
<wire x1="292" y1="125.08" x2="292" y2="128.89" width="0.1524" layer="91"/>
<label x="292" y="129.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="TP10" gate="G$1" pin="TP"/>
<wire x1="305" y1="127.46" x2="305" y2="123.65" width="0.1524" layer="91"/>
<label x="305" y="124.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_OUT_RAW" class="3">
<segment>
<pinref part="U7" gate="G$1" pin="OUT"/>
<wire x1="170.32" y1="127.46" x2="174.13" y2="127.46" width="0.1524" layer="91"/>
<label x="174.93" y="128.26" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R29" gate="G$1" pin="2"/>
<wire x1="255.08" y1="112" x2="258.89" y2="112" width="0.1524" layer="91"/>
<label x="259.69" y="112.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C21" gate="G$1" pin="2"/>
<wire x1="262" y1="98.92" x2="262" y2="95.11" width="0.1524" layer="91"/>
<label x="262" y="95.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R30" gate="G$1" pin="1"/>
<wire x1="274.92" y1="130" x2="271.11" y2="130" width="0.1524" layer="91"/>
<label x="270.31" y="130.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="ECG_RA" class="3">
<segment>
<pinref part="J7" gate="G$1" pin="2"/>
<wire x1="18.57" y1="165" x2="14.76" y2="165" width="0.1524" layer="91"/>
<label x="13.96" y="165.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R19" gate="G$1" pin="1"/>
<wire x1="54.92" y1="164" x2="51.11" y2="164" width="0.1524" layer="91"/>
<label x="50.31" y="164.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="ECG_RA_F" class="3">
<segment>
<pinref part="R19" gate="G$1" pin="2"/>
<wire x1="65.08" y1="164" x2="68.89" y2="164" width="0.1524" layer="91"/>
<label x="69.69" y="164.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U7" gate="G$1" pin="-IN"/>
<wire x1="129.68" y1="135.08" x2="125.87" y2="135.08" width="0.1524" layer="91"/>
<label x="125.07" y="135.88" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R22" gate="G$1" pin="2"/>
<wire x1="92" y1="190.08" x2="92" y2="193.89" width="0.1524" layer="91"/>
<label x="92" y="194.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_REFIN" class="3">
<segment>
<pinref part="U7" gate="G$1" pin="REFIN"/>
<wire x1="129.68" y1="127.46" x2="125.87" y2="127.46" width="0.1524" layer="91"/>
<label x="125.07" y="128.26" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R23" gate="G$1" pin="2"/>
<wire x1="112" y1="105.08" x2="112" y2="108.89" width="0.1524" layer="91"/>
<label x="112" y="109.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R24" gate="G$1" pin="1"/>
<wire x1="112" y1="79.92" x2="112" y2="76.11" width="0.1524" layer="91"/>
<label x="112" y="76.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C16" gate="G$1" pin="1"/>
<wire x1="124" y1="90.08" x2="124" y2="93.89" width="0.1524" layer="91"/>
<label x="124" y="94.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_REFOUT" class="3">
<segment>
<pinref part="U7" gate="G$1" pin="REFOUT"/>
<wire x1="129.68" y1="124.92" x2="125.87" y2="124.92" width="0.1524" layer="91"/>
<label x="125.07" y="125.72" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R26" gate="G$1" pin="1"/>
<wire x1="235" y1="159.92" x2="235" y2="156.11" width="0.1524" layer="91"/>
<label x="235" y="156.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C20" gate="G$1" pin="2"/>
<wire x1="262" y1="134.92" x2="262" y2="131.11" width="0.1524" layer="91"/>
<label x="262" y="131.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R28" gate="G$1" pin="2"/>
<wire x1="255.08" y1="120" x2="258.89" y2="120" width="0.1524" layer="91"/>
<label x="259.69" y="120.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="TP11" gate="G$1" pin="TP"/>
<wire x1="305" y1="117.46" x2="305" y2="113.65" width="0.1524" layer="91"/>
<label x="305" y="114.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_RL" class="3">
<segment>
<pinref part="J7" gate="G$1" pin="3"/>
<wire x1="18.57" y1="162.46" x2="14.76" y2="162.46" width="0.1524" layer="91"/>
<label x="13.96" y="163.26" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R20" gate="G$1" pin="2"/>
<wire x1="65.08" y1="150" x2="68.89" y2="150" width="0.1524" layer="91"/>
<label x="69.69" y="150.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_RLD" class="3">
<segment>
<pinref part="U7" gate="G$1" pin="RLD"/>
<wire x1="129.68" y1="130" x2="125.87" y2="130" width="0.1524" layer="91"/>
<label x="125.07" y="130.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="C17" gate="G$1" pin="1"/>
<wire x1="90" y1="145.08" x2="90" y2="148.89" width="0.1524" layer="91"/>
<label x="90" y="149.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R20" gate="G$1" pin="1"/>
<wire x1="54.92" y1="150" x2="51.11" y2="150" width="0.1524" layer="91"/>
<label x="50.31" y="150.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="ECG_RLDFB" class="0">
<segment>
<pinref part="U7" gate="G$1" pin="RLDFB"/>
<wire x1="129.68" y1="132.54" x2="125.87" y2="132.54" width="0.1524" layer="91"/>
<label x="125.07" y="133.34" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="C17" gate="G$1" pin="2"/>
<wire x1="90" y1="134.92" x2="90" y2="131.11" width="0.1524" layer="91"/>
<label x="90" y="131.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_SDN" class="0">
<segment>
<pinref part="U7" gate="G$1" pin="SDN"/>
<wire x1="129.68" y1="122.38" x2="125.87" y2="122.38" width="0.1524" layer="91"/>
<label x="125.07" y="123.18" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R31" gate="G$1" pin="2"/>
<wire x1="120" y1="165.08" x2="120" y2="168.89" width="0.1524" layer="91"/>
<label x="120" y="169.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="ECG_SW" class="3">
<segment>
<pinref part="U7" gate="G$1" pin="SW"/>
<wire x1="170.32" y1="135.08" x2="174.13" y2="135.08" width="0.1524" layer="91"/>
<label x="174.93" y="135.88" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C19" gate="G$1" pin="2"/>
<wire x1="220" y1="169.92" x2="220" y2="166.11" width="0.1524" layer="91"/>
<label x="220" y="166.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R26" gate="G$1" pin="2"/>
<wire x1="235" y1="170.08" x2="235" y2="173.89" width="0.1524" layer="91"/>
<label x="235" y="174.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R27" gate="G$1" pin="1"/>
<wire x1="244.92" y1="150" x2="241.11" y2="150" width="0.1524" layer="91"/>
<label x="240.31" y="150.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="GND" class="1">
<segment>
<pinref part="SUPPLY9" gate="G$1" pin="GND"/>
<wire x1="30" y1="62.54" x2="30" y2="66.35" width="0.1524" layer="91"/>
<label x="30" y="67.15" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U7" gate="G$1" pin="GND"/>
<wire x1="129.68" y1="140.16" x2="125.87" y2="140.16" width="0.1524" layer="91"/>
<label x="125.07" y="140.96" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U7" gate="G$1" pin="EP"/>
<wire x1="170.32" y1="119.84" x2="174.13" y2="119.84" width="0.1524" layer="91"/>
<label x="174.93" y="120.64" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U7" gate="G$1" pin="AC/DC"/>
<wire x1="129.68" y1="119.84" x2="125.87" y2="119.84" width="0.1524" layer="91"/>
<label x="125.07" y="120.64" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R24" gate="G$1" pin="2"/>
<wire x1="112" y1="90.08" x2="112" y2="93.89" width="0.1524" layer="91"/>
<label x="112" y="94.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C16" gate="G$1" pin="2"/>
<wire x1="124" y1="79.92" x2="124" y2="76.11" width="0.1524" layer="91"/>
<label x="124" y="76.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R32" gate="G$1" pin="2"/>
<wire x1="120" y1="145.08" x2="120" y2="148.89" width="0.1524" layer="91"/>
<label x="120" y="149.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C22" gate="G$1" pin="2"/>
<wire x1="292" y1="114.92" x2="292" y2="111.11" width="0.1524" layer="91"/>
<label x="292" y="111.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C23" gate="G$1" pin="2"/>
<wire x1="140" y1="184.92" x2="140" y2="181.11" width="0.1524" layer="91"/>
<label x="140" y="181.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C24" gate="G$1" pin="2"/>
<wire x1="152" y1="184.92" x2="152" y2="181.11" width="0.1524" layer="91"/>
<label x="152" y="181.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
</nets>
</sheet>
<sheet>
<description>SHEET 5/7 - MECHANICAL SENSING (LOAD CELL, FSR, STRETCH, PIEZO, HALL)</description>
<plain>
<wire x1="0" y1="0" x2="380" y2="0" width="0.3" layer="94"/>
<wire x1="380" y1="0" x2="380" y2="260" width="0.3" layer="94"/>
<wire x1="380" y1="260" x2="0" y2="260" width="0.3" layer="94"/>
<wire x1="0" y1="260" x2="0" y2="0" width="0.3" layer="94"/>
<wire x1="0" y1="22" x2="380" y2="22" width="0.3" layer="94"/>
<wire x1="0" y1="10" x2="380" y2="10" width="0.2" layer="94"/>
<text x="3" y="16" size="3" layer="94" ratio="10">SIH26113 - MATERNITY ASSIST BELT - PROTOTYPE CARRIER BOARD</text>
<text x="3" y="12" size="2" layer="94" ratio="10">SHEET 5/7 - MECHANICAL SENSING (LOAD CELL, FSR, STRETCH, PIEZO, HALL)</text>
<text x="3" y="5.5" size="1.8" layer="94" ratio="10">NOT A MEDICAL DEVICE. Prototype for engineering evaluation only. Human-connected ECG is NOT isolated - see documentation/README.</text>
<text x="3" y="2" size="1.8" layer="94" ratio="10">4-layer FR-4 1.6 mm (L1 sig / L2 GND plane / L15 3V3 plane / L16 sig) | board 100 x 70 mm | lib SIH26113_Maternity_Assist_Belt.lbr | sheet 5 of 7</text>
<text x="320" y="252" size="3.5" layer="94" ratio="10">SHEET 5/7</text>
<text x="30" y="200" size="2.6" layer="94" ratio="10">LOAD CELL BRIDGE</text>
<text x="110" y="200" size="2.6" layer="94" ratio="10">HX711 24-BIT ADC</text>
<text x="200" y="200" size="2.6" layer="94" ratio="10">FSR DIVIDERS</text>
<text x="250" y="160" size="2.6" layer="94" ratio="10">PIEZO CONDITIONING</text>
<text x="250" y="100" size="2.6" layer="94" ratio="10">HALL / LIMIT</text>
</plain>
<instances>
<instance part="U8" gate="G$1" x="110" y="160"/>
<instance part="J8" gate="G$1" x="30" y="165"/>
<instance part="C25" gate="G$1" x="78" y="140"/>
<instance part="C26" gate="G$1" x="88" y="175"/>
<instance part="C27" gate="G$1" x="98" y="175"/>
<instance part="C28" gate="G$1" x="68" y="175"/>
<instance part="TP12" gate="G$1" x="150" y="140"/>
<instance part="TP13" gate="G$1" x="160" y="140"/>
<instance part="J9" gate="G$1" x="190" y="185"/>
<instance part="R33" gate="G$1" x="200" y="168" rot="R90"/>
<instance part="C29" gate="G$1" x="212" y="168" rot="R90"/>
<instance part="J10" gate="G$1" x="220" y="185"/>
<instance part="R34" gate="G$1" x="230" y="168" rot="R90"/>
<instance part="C30" gate="G$1" x="242" y="168" rot="R90"/>
<instance part="J11" gate="G$1" x="250" y="185"/>
<instance part="R35" gate="G$1" x="260" y="168" rot="R90"/>
<instance part="C31" gate="G$1" x="272" y="168" rot="R90"/>
<instance part="J12" gate="G$1" x="280" y="185"/>
<instance part="R36" gate="G$1" x="290" y="168" rot="R90"/>
<instance part="C32" gate="G$1" x="302" y="168" rot="R90"/>
<instance part="J13" gate="G$1" x="190" y="130"/>
<instance part="R37" gate="G$1" x="202" y="115" rot="R90"/>
<instance part="C33" gate="G$1" x="214" y="115" rot="R90"/>
<instance part="J14" gate="G$1" x="250" y="130"/>
<instance part="R38" gate="G$1" x="258" y="115" rot="R90"/>
<instance part="C34" gate="G$1" x="268" y="130"/>
<instance part="R39" gate="G$1" x="282" y="145" rot="R90"/>
<instance part="R40" gate="G$1" x="282" y="118" rot="R90"/>
<instance part="R41" gate="G$1" x="296" y="130"/>
<instance part="C35" gate="G$1" x="308" y="118" rot="R90"/>
<instance part="D5" gate="G$1" x="320" y="140" rot="R90"/>
<instance part="D6" gate="G$1" x="320" y="118" rot="R90"/>
<instance part="J15" gate="G$1" x="250" y="80"/>
<instance part="R42" gate="G$1" x="262" y="95" rot="R90"/>
<instance part="C36" gate="G$1" x="274" y="68" rot="R90"/>
<instance part="TP14" gate="G$1" x="340" y="100"/>
<instance part="SUPPLY11" gate="G$1" x="30" y="40"/>
<instance part="SUPPLY12" gate="G$1" x="45" y="40"/>
</instances>
<busses/>
<nets>
<net name="3V3" class="1">
<segment>
<pinref part="SUPPLY12" gate="G$1" pin="3V3"/>
<wire x1="45" y1="40" x2="45" y2="36.19" width="0.1524" layer="91"/>
<label x="45" y="36.99" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U8" gate="G$1" pin="VSUP"/>
<wire x1="90.95" y1="170.16" x2="87.14" y2="170.16" width="0.1524" layer="91"/>
<label x="86.34" y="170.96" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U8" gate="G$1" pin="AVDD"/>
<wire x1="90.95" y1="167.62" x2="87.14" y2="167.62" width="0.1524" layer="91"/>
<label x="86.34" y="168.42" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U8" gate="G$1" pin="DVDD"/>
<wire x1="90.95" y1="165.08" x2="87.14" y2="165.08" width="0.1524" layer="91"/>
<label x="86.34" y="165.88" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="J8" gate="G$1" pin="1"/>
<wire x1="18.57" y1="168.81" x2="14.76" y2="168.81" width="0.1524" layer="91"/>
<label x="13.96" y="169.61" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="C26" gate="G$1" pin="1"/>
<wire x1="88" y1="180.08" x2="88" y2="183.89" width="0.1524" layer="91"/>
<label x="88" y="184.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C27" gate="G$1" pin="1"/>
<wire x1="98" y1="180.08" x2="98" y2="183.89" width="0.1524" layer="91"/>
<label x="98" y="184.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C28" gate="G$1" pin="1"/>
<wire x1="68" y1="180.08" x2="68" y2="183.89" width="0.1524" layer="91"/>
<label x="68" y="184.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J9" gate="G$1" pin="1"/>
<wire x1="178.57" y1="186.27" x2="174.76" y2="186.27" width="0.1524" layer="91"/>
<label x="173.96" y="187.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="J10" gate="G$1" pin="1"/>
<wire x1="208.57" y1="186.27" x2="204.76" y2="186.27" width="0.1524" layer="91"/>
<label x="203.96" y="187.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="J11" gate="G$1" pin="1"/>
<wire x1="238.57" y1="186.27" x2="234.76" y2="186.27" width="0.1524" layer="91"/>
<label x="233.96" y="187.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="J12" gate="G$1" pin="1"/>
<wire x1="268.57" y1="186.27" x2="264.76" y2="186.27" width="0.1524" layer="91"/>
<label x="263.96" y="187.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="J13" gate="G$1" pin="1"/>
<wire x1="178.57" y1="131.27" x2="174.76" y2="131.27" width="0.1524" layer="91"/>
<label x="173.96" y="132.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R39" gate="G$1" pin="1"/>
<wire x1="282" y1="139.92" x2="282" y2="136.11" width="0.1524" layer="91"/>
<label x="282" y="136.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="D5" gate="G$1" pin="C"/>
<wire x1="320" y1="136.19" x2="320" y2="132.38" width="0.1524" layer="91"/>
<label x="320" y="133.18" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J15" gate="G$1" pin="1"/>
<wire x1="238.57" y1="82.54" x2="234.76" y2="82.54" width="0.1524" layer="91"/>
<label x="233.96" y="83.34" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R42" gate="G$1" pin="1"/>
<wire x1="262" y1="89.92" x2="262" y2="86.11" width="0.1524" layer="91"/>
<label x="262" y="86.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="FSR1_ADC" class="0">
<segment>
<pinref part="J9" gate="G$1" pin="2"/>
<wire x1="178.57" y1="183.73" x2="174.76" y2="183.73" width="0.1524" layer="91"/>
<label x="173.96" y="184.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R33" gate="G$1" pin="1"/>
<wire x1="200" y1="162.92" x2="200" y2="159.11" width="0.1524" layer="91"/>
<label x="200" y="159.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C29" gate="G$1" pin="1"/>
<wire x1="206.92" y1="168" x2="203.11" y2="168" width="0.1524" layer="91"/>
<label x="202.31" y="168.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="FSR2_ADC" class="0">
<segment>
<pinref part="J10" gate="G$1" pin="2"/>
<wire x1="208.57" y1="183.73" x2="204.76" y2="183.73" width="0.1524" layer="91"/>
<label x="203.96" y="184.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R34" gate="G$1" pin="1"/>
<wire x1="230" y1="162.92" x2="230" y2="159.11" width="0.1524" layer="91"/>
<label x="230" y="159.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C30" gate="G$1" pin="1"/>
<wire x1="236.92" y1="168" x2="233.11" y2="168" width="0.1524" layer="91"/>
<label x="232.31" y="168.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="FSR3_ADC" class="0">
<segment>
<pinref part="J11" gate="G$1" pin="2"/>
<wire x1="238.57" y1="183.73" x2="234.76" y2="183.73" width="0.1524" layer="91"/>
<label x="233.96" y="184.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R35" gate="G$1" pin="1"/>
<wire x1="260" y1="162.92" x2="260" y2="159.11" width="0.1524" layer="91"/>
<label x="260" y="159.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C31" gate="G$1" pin="1"/>
<wire x1="266.92" y1="168" x2="263.11" y2="168" width="0.1524" layer="91"/>
<label x="262.31" y="168.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="FSR4_ADC" class="0">
<segment>
<pinref part="J12" gate="G$1" pin="2"/>
<wire x1="268.57" y1="183.73" x2="264.76" y2="183.73" width="0.1524" layer="91"/>
<label x="263.96" y="184.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R36" gate="G$1" pin="1"/>
<wire x1="290" y1="162.92" x2="290" y2="159.11" width="0.1524" layer="91"/>
<label x="290" y="159.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C32" gate="G$1" pin="1"/>
<wire x1="296.92" y1="168" x2="293.11" y2="168" width="0.1524" layer="91"/>
<label x="292.31" y="168.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="GND" class="1">
<segment>
<pinref part="SUPPLY11" gate="G$1" pin="GND"/>
<wire x1="30" y1="42.54" x2="30" y2="46.35" width="0.1524" layer="91"/>
<label x="30" y="47.15" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U8" gate="G$1" pin="AGND"/>
<wire x1="90.95" y1="162.54" x2="87.14" y2="162.54" width="0.1524" layer="91"/>
<label x="86.34" y="163.34" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U8" gate="G$1" pin="VFB"/>
<wire x1="90.95" y1="157.46" x2="87.14" y2="157.46" width="0.1524" layer="91"/>
<label x="86.34" y="158.26" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U8" gate="G$1" pin="INB+"/>
<wire x1="129.05" y1="165.08" x2="132.86" y2="165.08" width="0.1524" layer="91"/>
<label x="133.66" y="165.88" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U8" gate="G$1" pin="INB-"/>
<wire x1="129.05" y1="162.54" x2="132.86" y2="162.54" width="0.1524" layer="91"/>
<label x="133.66" y="163.34" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U8" gate="G$1" pin="XI"/>
<wire x1="129.05" y1="154.92" x2="132.86" y2="154.92" width="0.1524" layer="91"/>
<label x="133.66" y="155.72" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="U8" gate="G$1" pin="RATE"/>
<wire x1="129.05" y1="149.84" x2="132.86" y2="149.84" width="0.1524" layer="91"/>
<label x="133.66" y="150.64" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J8" gate="G$1" pin="2"/>
<wire x1="18.57" y1="166.27" x2="14.76" y2="166.27" width="0.1524" layer="91"/>
<label x="13.96" y="167.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="C25" gate="G$1" pin="2"/>
<wire x1="78" y1="134.92" x2="78" y2="131.11" width="0.1524" layer="91"/>
<label x="78" y="131.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C26" gate="G$1" pin="2"/>
<wire x1="88" y1="169.92" x2="88" y2="166.11" width="0.1524" layer="91"/>
<label x="88" y="166.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C27" gate="G$1" pin="2"/>
<wire x1="98" y1="169.92" x2="98" y2="166.11" width="0.1524" layer="91"/>
<label x="98" y="166.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C28" gate="G$1" pin="2"/>
<wire x1="68" y1="169.92" x2="68" y2="166.11" width="0.1524" layer="91"/>
<label x="68" y="166.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R33" gate="G$1" pin="2"/>
<wire x1="200" y1="173.08" x2="200" y2="176.89" width="0.1524" layer="91"/>
<label x="200" y="177.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R34" gate="G$1" pin="2"/>
<wire x1="230" y1="173.08" x2="230" y2="176.89" width="0.1524" layer="91"/>
<label x="230" y="177.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R35" gate="G$1" pin="2"/>
<wire x1="260" y1="173.08" x2="260" y2="176.89" width="0.1524" layer="91"/>
<label x="260" y="177.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R36" gate="G$1" pin="2"/>
<wire x1="290" y1="173.08" x2="290" y2="176.89" width="0.1524" layer="91"/>
<label x="290" y="177.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C29" gate="G$1" pin="2"/>
<wire x1="217.08" y1="168" x2="220.89" y2="168" width="0.1524" layer="91"/>
<label x="221.69" y="168.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C30" gate="G$1" pin="2"/>
<wire x1="247.08" y1="168" x2="250.89" y2="168" width="0.1524" layer="91"/>
<label x="251.69" y="168.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C31" gate="G$1" pin="2"/>
<wire x1="277.08" y1="168" x2="280.89" y2="168" width="0.1524" layer="91"/>
<label x="281.69" y="168.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C32" gate="G$1" pin="2"/>
<wire x1="307.08" y1="168" x2="310.89" y2="168" width="0.1524" layer="91"/>
<label x="311.69" y="168.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R37" gate="G$1" pin="2"/>
<wire x1="202" y1="120.08" x2="202" y2="123.89" width="0.1524" layer="91"/>
<label x="202" y="124.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C33" gate="G$1" pin="2"/>
<wire x1="219.08" y1="115" x2="222.89" y2="115" width="0.1524" layer="91"/>
<label x="223.69" y="115.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J14" gate="G$1" pin="2"/>
<wire x1="238.57" y1="128.73" x2="234.76" y2="128.73" width="0.1524" layer="91"/>
<label x="233.96" y="129.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R38" gate="G$1" pin="2"/>
<wire x1="258" y1="120.08" x2="258" y2="123.89" width="0.1524" layer="91"/>
<label x="258" y="124.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R40" gate="G$1" pin="2"/>
<wire x1="282" y1="123.08" x2="282" y2="126.89" width="0.1524" layer="91"/>
<label x="282" y="127.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C35" gate="G$1" pin="2"/>
<wire x1="313.08" y1="118" x2="316.89" y2="118" width="0.1524" layer="91"/>
<label x="317.69" y="118.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="D6" gate="G$1" pin="A"/>
<wire x1="320" y1="121.81" x2="320" y2="125.62" width="0.1524" layer="91"/>
<label x="320" y="126.42" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J15" gate="G$1" pin="3"/>
<wire x1="238.57" y1="77.46" x2="234.76" y2="77.46" width="0.1524" layer="91"/>
<label x="233.96" y="78.26" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="C36" gate="G$1" pin="2"/>
<wire x1="279.08" y1="68" x2="282.89" y2="68" width="0.1524" layer="91"/>
<label x="283.69" y="68.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="HALL_LIMIT" class="0">
<segment>
<pinref part="J15" gate="G$1" pin="2"/>
<wire x1="238.57" y1="80" x2="234.76" y2="80" width="0.1524" layer="91"/>
<label x="233.96" y="80.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R42" gate="G$1" pin="2"/>
<wire x1="262" y1="100.08" x2="262" y2="103.89" width="0.1524" layer="91"/>
<label x="262" y="104.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C36" gate="G$1" pin="1"/>
<wire x1="268.92" y1="68" x2="265.11" y2="68" width="0.1524" layer="91"/>
<label x="264.31" y="68.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="HX_BASE" class="0">
<segment>
<pinref part="U8" gate="G$1" pin="BASE"/>
<wire x1="90.95" y1="160" x2="87.14" y2="160" width="0.1524" layer="91"/>
<label x="86.34" y="160.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="TP12" gate="G$1" pin="TP"/>
<wire x1="150" y1="137.46" x2="150" y2="133.65" width="0.1524" layer="91"/>
<label x="150" y="134.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="HX_DOUT" class="0">
<segment>
<pinref part="U8" gate="G$1" pin="DOUT"/>
<wire x1="129.05" y1="157.46" x2="132.86" y2="157.46" width="0.1524" layer="91"/>
<label x="133.66" y="158.26" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="TP14" gate="G$1" pin="TP"/>
<wire x1="340" y1="97.46" x2="340" y2="93.65" width="0.1524" layer="91"/>
<label x="340" y="94.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="HX_SCK" class="0">
<segment>
<pinref part="U8" gate="G$1" pin="PD_SCK"/>
<wire x1="129.05" y1="160" x2="132.86" y2="160" width="0.1524" layer="91"/>
<label x="133.66" y="160.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="HX_VBG" class="0">
<segment>
<pinref part="U8" gate="G$1" pin="VBG"/>
<wire x1="90.95" y1="154.92" x2="87.14" y2="154.92" width="0.1524" layer="91"/>
<label x="86.34" y="155.72" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="C25" gate="G$1" pin="1"/>
<wire x1="78" y1="145.08" x2="78" y2="148.89" width="0.1524" layer="91"/>
<label x="78" y="149.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="HX_XO" class="0">
<segment>
<pinref part="U8" gate="G$1" pin="XO"/>
<wire x1="129.05" y1="152.38" x2="132.86" y2="152.38" width="0.1524" layer="91"/>
<label x="133.66" y="153.18" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="TP13" gate="G$1" pin="TP"/>
<wire x1="160" y1="137.46" x2="160" y2="133.65" width="0.1524" layer="91"/>
<label x="160" y="134.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="LC_A_N" class="0">
<segment>
<pinref part="J8" gate="G$1" pin="4"/>
<wire x1="18.57" y1="161.19" x2="14.76" y2="161.19" width="0.1524" layer="91"/>
<label x="13.96" y="161.99" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U8" gate="G$1" pin="INA-"/>
<wire x1="129.05" y1="167.62" x2="132.86" y2="167.62" width="0.1524" layer="91"/>
<label x="133.66" y="168.42" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="LC_A_P" class="0">
<segment>
<pinref part="J8" gate="G$1" pin="3"/>
<wire x1="18.57" y1="163.73" x2="14.76" y2="163.73" width="0.1524" layer="91"/>
<label x="13.96" y="164.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="U8" gate="G$1" pin="INA+"/>
<wire x1="129.05" y1="170.16" x2="132.86" y2="170.16" width="0.1524" layer="91"/>
<label x="133.66" y="170.96" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="PIEZO_AC" class="0">
<segment>
<pinref part="C34" gate="G$1" pin="2"/>
<wire x1="268" y1="124.92" x2="268" y2="121.11" width="0.1524" layer="91"/>
<label x="268" y="121.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R39" gate="G$1" pin="2"/>
<wire x1="282" y1="150.08" x2="282" y2="153.89" width="0.1524" layer="91"/>
<label x="282" y="154.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R40" gate="G$1" pin="1"/>
<wire x1="282" y1="112.92" x2="282" y2="109.11" width="0.1524" layer="91"/>
<label x="282" y="109.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R41" gate="G$1" pin="1"/>
<wire x1="290.92" y1="130" x2="287.11" y2="130" width="0.1524" layer="91"/>
<label x="286.31" y="130.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="PIEZO_ADC" class="0">
<segment>
<pinref part="R41" gate="G$1" pin="2"/>
<wire x1="301.08" y1="130" x2="304.89" y2="130" width="0.1524" layer="91"/>
<label x="305.69" y="130.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C35" gate="G$1" pin="1"/>
<wire x1="302.92" y1="118" x2="299.11" y2="118" width="0.1524" layer="91"/>
<label x="298.31" y="118.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="D5" gate="G$1" pin="A"/>
<wire x1="320" y1="143.81" x2="320" y2="147.62" width="0.1524" layer="91"/>
<label x="320" y="148.42" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="D6" gate="G$1" pin="C"/>
<wire x1="320" y1="114.19" x2="320" y2="110.38" width="0.1524" layer="91"/>
<label x="320" y="111.18" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="PIEZO_IN" class="0">
<segment>
<pinref part="J14" gate="G$1" pin="1"/>
<wire x1="238.57" y1="131.27" x2="234.76" y2="131.27" width="0.1524" layer="91"/>
<label x="233.96" y="132.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R38" gate="G$1" pin="1"/>
<wire x1="258" y1="109.92" x2="258" y2="106.11" width="0.1524" layer="91"/>
<label x="258" y="106.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C34" gate="G$1" pin="1"/>
<wire x1="268" y1="135.08" x2="268" y2="138.89" width="0.1524" layer="91"/>
<label x="268" y="139.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="STRETCH_ADC" class="0">
<segment>
<pinref part="J13" gate="G$1" pin="2"/>
<wire x1="178.57" y1="128.73" x2="174.76" y2="128.73" width="0.1524" layer="91"/>
<label x="173.96" y="129.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R37" gate="G$1" pin="1"/>
<wire x1="202" y1="109.92" x2="202" y2="106.11" width="0.1524" layer="91"/>
<label x="202" y="106.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C33" gate="G$1" pin="1"/>
<wire x1="208.92" y1="115" x2="205.11" y2="115" width="0.1524" layer="91"/>
<label x="204.31" y="115.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
</nets>
</sheet>
<sheet>
<description>SHEET 6/7 - FET-DRIVEN ALERTS (VIBRATION MOTOR, BUZZER)</description>
<plain>
<wire x1="0" y1="0" x2="380" y2="0" width="0.3" layer="94"/>
<wire x1="380" y1="0" x2="380" y2="260" width="0.3" layer="94"/>
<wire x1="380" y1="260" x2="0" y2="260" width="0.3" layer="94"/>
<wire x1="0" y1="260" x2="0" y2="0" width="0.3" layer="94"/>
<wire x1="0" y1="22" x2="380" y2="22" width="0.3" layer="94"/>
<wire x1="0" y1="10" x2="380" y2="10" width="0.2" layer="94"/>
<text x="3" y="16" size="3" layer="94" ratio="10">SIH26113 - MATERNITY ASSIST BELT - PROTOTYPE CARRIER BOARD</text>
<text x="3" y="12" size="2" layer="94" ratio="10">SHEET 6/7 - FET-DRIVEN ALERTS (VIBRATION MOTOR, BUZZER)</text>
<text x="3" y="5.5" size="1.8" layer="94" ratio="10">NOT A MEDICAL DEVICE. Prototype for engineering evaluation only. Human-connected ECG is NOT isolated - see documentation/README.</text>
<text x="3" y="2" size="1.8" layer="94" ratio="10">4-layer FR-4 1.6 mm (L1 sig / L2 GND plane / L15 3V3 plane / L16 sig) | board 100 x 70 mm | lib SIH26113_Maternity_Assist_Belt.lbr | sheet 6 of 7</text>
<text x="320" y="252" size="3.5" layer="94" ratio="10">SHEET 6/7</text>
<text x="85" y="200" size="2.6" layer="94" ratio="10">MOTOR DRIVER</text>
<text x="85" y="135" size="2.6" layer="94" ratio="10">BUZZER DRIVER</text>
</plain>
<instances>
<instance part="Q1" gate="G$1" x="110" y="165"/>
<instance part="R43" gate="G$1" x="85" y="165"/>
<instance part="R44" gate="G$1" x="97" y="150" rot="R90"/>
<instance part="J16" gate="G$1" x="150" y="190"/>
<instance part="R45" gate="G$1" x="130" y="195"/>
<instance part="D7" gate="G$1" x="140" y="175" rot="R90"/>
<instance part="C37" gate="G$1" x="122" y="175"/>
<instance part="Q2" gate="G$1" x="110" y="100"/>
<instance part="R46" gate="G$1" x="85" y="100"/>
<instance part="R47" gate="G$1" x="97" y="85" rot="R90"/>
<instance part="J17" gate="G$1" x="150" y="125"/>
<instance part="D8" gate="G$1" x="140" y="110" rot="R90"/>
<instance part="C38" gate="G$1" x="122" y="110"/>
<instance part="TP15" gate="G$1" x="200" y="150"/>
<instance part="TP16" gate="G$1" x="210" y="150"/>
<instance part="SUPPLY13" gate="G$1" x="30" y="50"/>
<instance part="SUPPLY14" gate="G$1" x="45" y="50"/>
<instance part="SUPPLY15" gate="G$1" x="60" y="50"/>
</instances>
<busses/>
<nets>
<net name="3V3" class="1">
<segment>
<pinref part="SUPPLY14" gate="G$1" pin="3V3"/>
<wire x1="45" y1="50" x2="45" y2="46.19" width="0.1524" layer="91"/>
<label x="45" y="46.99" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J17" gate="G$1" pin="1"/>
<wire x1="138.57" y1="126.27" x2="134.76" y2="126.27" width="0.1524" layer="91"/>
<label x="133.96" y="127.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="D8" gate="G$1" pin="C"/>
<wire x1="140" y1="106.19" x2="140" y2="102.38" width="0.1524" layer="91"/>
<label x="140" y="103.18" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C38" gate="G$1" pin="1"/>
<wire x1="122" y1="115.08" x2="122" y2="118.89" width="0.1524" layer="91"/>
<label x="122" y="119.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="BUZZER_EN" class="0">
<segment>
<pinref part="R46" gate="G$1" pin="1"/>
<wire x1="79.92" y1="100" x2="76.11" y2="100" width="0.1524" layer="91"/>
<label x="75.31" y="100.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="TP16" gate="G$1" pin="TP"/>
<wire x1="210" y1="147.46" x2="210" y2="143.65" width="0.1524" layer="91"/>
<label x="210" y="144.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="BUZZ_G" class="0">
<segment>
<pinref part="R46" gate="G$1" pin="2"/>
<wire x1="90.08" y1="100" x2="93.89" y2="100" width="0.1524" layer="91"/>
<label x="94.69" y="100.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="Q2" gate="G$1" pin="G"/>
<wire x1="104.92" y1="100" x2="101.11" y2="100" width="0.1524" layer="91"/>
<label x="100.31" y="100.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R47" gate="G$1" pin="1"/>
<wire x1="97" y1="79.92" x2="97" y2="76.11" width="0.1524" layer="91"/>
<label x="97" y="76.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="BUZZ_N" class="0">
<segment>
<pinref part="J17" gate="G$1" pin="2"/>
<wire x1="138.57" y1="123.73" x2="134.76" y2="123.73" width="0.1524" layer="91"/>
<label x="133.96" y="124.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="Q2" gate="G$1" pin="D"/>
<wire x1="112.54" y1="106.35" x2="112.54" y2="110.16" width="0.1524" layer="91"/>
<label x="112.54" y="110.96" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="D8" gate="G$1" pin="A"/>
<wire x1="140" y1="113.81" x2="140" y2="117.62" width="0.1524" layer="91"/>
<label x="140" y="118.42" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="GND" class="1">
<segment>
<pinref part="SUPPLY13" gate="G$1" pin="GND"/>
<wire x1="30" y1="52.54" x2="30" y2="56.35" width="0.1524" layer="91"/>
<label x="30" y="57.15" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="Q1" gate="G$1" pin="S"/>
<wire x1="112.54" y1="158.65" x2="112.54" y2="154.84" width="0.1524" layer="91"/>
<label x="112.54" y="155.64" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R44" gate="G$1" pin="2"/>
<wire x1="97" y1="155.08" x2="97" y2="158.89" width="0.1524" layer="91"/>
<label x="97" y="159.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="Q2" gate="G$1" pin="S"/>
<wire x1="112.54" y1="93.65" x2="112.54" y2="89.84" width="0.1524" layer="91"/>
<label x="112.54" y="90.64" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R47" gate="G$1" pin="2"/>
<wire x1="97" y1="90.08" x2="97" y2="93.89" width="0.1524" layer="91"/>
<label x="97" y="94.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C37" gate="G$1" pin="2"/>
<wire x1="122" y1="169.92" x2="122" y2="166.11" width="0.1524" layer="91"/>
<label x="122" y="166.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C38" gate="G$1" pin="2"/>
<wire x1="122" y1="104.92" x2="122" y2="101.11" width="0.1524" layer="91"/>
<label x="122" y="101.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="MOTOR_EN" class="0">
<segment>
<pinref part="R43" gate="G$1" pin="1"/>
<wire x1="79.92" y1="165" x2="76.11" y2="165" width="0.1524" layer="91"/>
<label x="75.31" y="165.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="TP15" gate="G$1" pin="TP"/>
<wire x1="200" y1="147.46" x2="200" y2="143.65" width="0.1524" layer="91"/>
<label x="200" y="144.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="MOTOR_G" class="0">
<segment>
<pinref part="R43" gate="G$1" pin="2"/>
<wire x1="90.08" y1="165" x2="93.89" y2="165" width="0.1524" layer="91"/>
<label x="94.69" y="165.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="Q1" gate="G$1" pin="G"/>
<wire x1="104.92" y1="165" x2="101.11" y2="165" width="0.1524" layer="91"/>
<label x="100.31" y="165.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R44" gate="G$1" pin="1"/>
<wire x1="97" y1="144.92" x2="97" y2="141.11" width="0.1524" layer="91"/>
<label x="97" y="141.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="MOTOR_N" class="2">
<segment>
<pinref part="J16" gate="G$1" pin="2"/>
<wire x1="138.57" y1="188.73" x2="134.76" y2="188.73" width="0.1524" layer="91"/>
<label x="133.96" y="189.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="Q1" gate="G$1" pin="D"/>
<wire x1="112.54" y1="171.35" x2="112.54" y2="175.16" width="0.1524" layer="91"/>
<label x="112.54" y="175.96" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="D7" gate="G$1" pin="A"/>
<wire x1="140" y1="178.81" x2="140" y2="182.62" width="0.1524" layer="91"/>
<label x="140" y="183.42" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="MOTOR_P" class="2">
<segment>
<pinref part="R45" gate="G$1" pin="2"/>
<wire x1="135.08" y1="195" x2="138.89" y2="195" width="0.1524" layer="91"/>
<label x="139.69" y="195.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J16" gate="G$1" pin="1"/>
<wire x1="138.57" y1="191.27" x2="134.76" y2="191.27" width="0.1524" layer="91"/>
<label x="133.96" y="192.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="D7" gate="G$1" pin="C"/>
<wire x1="140" y1="171.19" x2="140" y2="167.38" width="0.1524" layer="91"/>
<label x="140" y="168.18" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C37" gate="G$1" pin="1"/>
<wire x1="122" y1="180.08" x2="122" y2="183.89" width="0.1524" layer="91"/>
<label x="122" y="184.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="VBAT" class="1">
<segment>
<pinref part="SUPPLY15" gate="G$1" pin="VBAT"/>
<wire x1="60" y1="50" x2="60" y2="46.19" width="0.1524" layer="91"/>
<label x="60" y="46.99" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R45" gate="G$1" pin="1"/>
<wire x1="124.92" y1="195" x2="121.11" y2="195" width="0.1524" layer="91"/>
<label x="120.31" y="195.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
</nets>
</sheet>
<sheet>
<description>SHEET 7/7 - USER INPUT AND STORAGE (SOS, microSD)</description>
<plain>
<wire x1="0" y1="0" x2="380" y2="0" width="0.3" layer="94"/>
<wire x1="380" y1="0" x2="380" y2="260" width="0.3" layer="94"/>
<wire x1="380" y1="260" x2="0" y2="260" width="0.3" layer="94"/>
<wire x1="0" y1="260" x2="0" y2="0" width="0.3" layer="94"/>
<wire x1="0" y1="22" x2="380" y2="22" width="0.3" layer="94"/>
<wire x1="0" y1="10" x2="380" y2="10" width="0.2" layer="94"/>
<text x="3" y="16" size="3" layer="94" ratio="10">SIH26113 - MATERNITY ASSIST BELT - PROTOTYPE CARRIER BOARD</text>
<text x="3" y="12" size="2" layer="94" ratio="10">SHEET 7/7 - USER INPUT AND STORAGE (SOS, microSD)</text>
<text x="3" y="5.5" size="1.8" layer="94" ratio="10">NOT A MEDICAL DEVICE. Prototype for engineering evaluation only. Human-connected ECG is NOT isolated - see documentation/README.</text>
<text x="3" y="2" size="1.8" layer="94" ratio="10">4-layer FR-4 1.6 mm (L1 sig / L2 GND plane / L15 3V3 plane / L16 sig) | board 100 x 70 mm | lib SIH26113_Maternity_Assist_Belt.lbr | sheet 7 of 7</text>
<text x="320" y="252" size="3.5" layer="94" ratio="10">SHEET 7/7</text>
<text x="55" y="195" size="2.6" layer="94" ratio="10">SOS BUTTON</text>
<text x="185" y="195" size="2.6" layer="94" ratio="10">microSD (SPI MODULE)</text>
</plain>
<instances>
<instance part="SW4" gate="G$1" x="60" y="165"/>
<instance part="R48" gate="G$1" x="48" y="185" rot="R90"/>
<instance part="C39" gate="G$1" x="78" y="150" rot="R90"/>
<instance part="R49" gate="G$1" x="92" y="165"/>
<instance part="J18" gate="G$1" x="190" y="160"/>
<instance part="R50" gate="G$1" x="165" y="185" rot="R90"/>
<instance part="R51" gate="G$1" x="177" y="185" rot="R90"/>
<instance part="TP17" gate="G$1" x="240" y="140"/>
<instance part="TP18" gate="G$1" x="250" y="140"/>
<instance part="TP19" gate="G$1" x="260" y="140"/>
<instance part="SUPPLY16" gate="G$1" x="30" y="60"/>
<instance part="SUPPLY17" gate="G$1" x="45" y="60"/>
</instances>
<busses/>
<nets>
<net name="3V3" class="1">
<segment>
<pinref part="SUPPLY17" gate="G$1" pin="3V3"/>
<wire x1="45" y1="60" x2="45" y2="56.19" width="0.1524" layer="91"/>
<label x="45" y="56.99" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R48" gate="G$1" pin="1"/>
<wire x1="48" y1="179.92" x2="48" y2="176.11" width="0.1524" layer="91"/>
<label x="48" y="176.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J18" gate="G$1" pin="1"/>
<wire x1="178.57" y1="166.35" x2="174.76" y2="166.35" width="0.1524" layer="91"/>
<label x="173.96" y="167.15" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R50" gate="G$1" pin="1"/>
<wire x1="165" y1="179.92" x2="165" y2="176.11" width="0.1524" layer="91"/>
<label x="165" y="176.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="R51" gate="G$1" pin="1"/>
<wire x1="177" y1="179.92" x2="177" y2="176.11" width="0.1524" layer="91"/>
<label x="177" y="176.91" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="GND" class="1">
<segment>
<pinref part="SUPPLY16" gate="G$1" pin="GND"/>
<wire x1="30" y1="62.54" x2="30" y2="66.35" width="0.1524" layer="91"/>
<label x="30" y="67.15" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="SW4" gate="G$1" pin="N"/>
<wire x1="65.08" y1="165" x2="68.89" y2="165" width="0.1524" layer="91"/>
<label x="69.69" y="165.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C39" gate="G$1" pin="2"/>
<wire x1="83.08" y1="150" x2="86.89" y2="150" width="0.1524" layer="91"/>
<label x="87.69" y="150.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="J18" gate="G$1" pin="2"/>
<wire x1="178.57" y1="163.81" x2="174.76" y2="163.81" width="0.1524" layer="91"/>
<label x="173.96" y="164.61" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="I2C_SCL" class="0">
<segment>
<pinref part="TP19" gate="G$1" pin="TP"/>
<wire x1="260" y1="137.46" x2="260" y2="133.65" width="0.1524" layer="91"/>
<label x="260" y="134.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="I2C_SDA" class="0">
<segment>
<pinref part="TP18" gate="G$1" pin="TP"/>
<wire x1="250" y1="137.46" x2="250" y2="133.65" width="0.1524" layer="91"/>
<label x="250" y="134.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="SD_CS" class="0">
<segment>
<pinref part="J18" gate="G$1" pin="6"/>
<wire x1="178.57" y1="153.65" x2="174.76" y2="153.65" width="0.1524" layer="91"/>
<label x="173.96" y="154.45" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R50" gate="G$1" pin="2"/>
<wire x1="165" y1="190.08" x2="165" y2="193.89" width="0.1524" layer="91"/>
<label x="165" y="194.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="SD_MISO" class="0">
<segment>
<pinref part="J18" gate="G$1" pin="5"/>
<wire x1="178.57" y1="156.19" x2="174.76" y2="156.19" width="0.1524" layer="91"/>
<label x="173.96" y="156.99" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R51" gate="G$1" pin="2"/>
<wire x1="177" y1="190.08" x2="177" y2="193.89" width="0.1524" layer="91"/>
<label x="177" y="194.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
<net name="SD_MOSI" class="0">
<segment>
<pinref part="J18" gate="G$1" pin="4"/>
<wire x1="178.57" y1="158.73" x2="174.76" y2="158.73" width="0.1524" layer="91"/>
<label x="173.96" y="159.53" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="SD_SCK" class="0">
<segment>
<pinref part="J18" gate="G$1" pin="3"/>
<wire x1="178.57" y1="161.27" x2="174.76" y2="161.27" width="0.1524" layer="91"/>
<label x="173.96" y="162.07" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="SOS_BTN" class="0">
<segment>
<pinref part="SW4" gate="G$1" pin="P"/>
<wire x1="54.92" y1="165" x2="51.11" y2="165" width="0.1524" layer="91"/>
<label x="50.31" y="165.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R48" gate="G$1" pin="2"/>
<wire x1="48" y1="190.08" x2="48" y2="193.89" width="0.1524" layer="91"/>
<label x="48" y="194.69" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="C39" gate="G$1" pin="1"/>
<wire x1="72.92" y1="150" x2="69.11" y2="150" width="0.1524" layer="91"/>
<label x="68.31" y="150.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
<segment>
<pinref part="R49" gate="G$1" pin="1"/>
<wire x1="86.92" y1="165" x2="83.11" y2="165" width="0.1524" layer="91"/>
<label x="82.31" y="165.8" size="1.27" layer="95" rot="R0" align="bottom-right" xref="yes"/>
</segment>
</net>
<net name="SOS_GPIO" class="0">
<segment>
<pinref part="R49" gate="G$1" pin="2"/>
<wire x1="97.08" y1="165" x2="100.89" y2="165" width="0.1524" layer="91"/>
<label x="101.69" y="165.8" size="1.27" layer="95" rot="R0" align="bottom-left" xref="yes"/>
</segment>
<segment>
<pinref part="TP17" gate="G$1" pin="TP"/>
<wire x1="240" y1="137.46" x2="240" y2="133.65" width="0.1524" layer="91"/>
<label x="240" y="134.45" size="1.27" layer="95" rot="R90" align="bottom-left" xref="yes"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
