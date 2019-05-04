# LSS

Lss is an alternative to `ls` command in linux which prints sequences instead of
just printing file names in the directory.

**Example**:

> \>ls  
>elem.info sd_fx29.0112.rgb sd_fx29.0125.rgb sd_fx29.0137.rgb
>sd_fx29.0101.rgb sd_fx29.0113.rgb sd_fx29.0126.rgb sd_fx29.0138.rgb
>sd_fx29.0102.rgb sd_fx29.0114.rgb sd_fx29.0127.rgb sd_fx29.0139.rgb
>sd_fx29.0103.rgb sd_fx29.0115.rgb sd_fx29.0128.rgb sd_fx29.0140.rgb
>sd_fx29.0104.rgb sd_fx29.0116.rgb sd_fx29.0129.rgb sd_fx29.0141.rgb
>sd_fx29.0105.rgb sd_fx29.0117.rgb sd_fx29.0130.rgb sd_fx29.0142.rgb
>sd_fx29.0106.rgb sd_fx29.0118.rgb sd_fx29.0131.rgb sd_fx29.0143.rgb
>sd_fx29.0107.rgb sd_fx29.0119.rgb sd_fx29.0132.rgb sd_fx29.0144.rgb
>sd_fx29.0108.rgb sd_fx29.0120.rgb sd_fx29.0133.rgb sd_fx29.0145.rgb
>sd_fx29.0109.rgb sd_fx29.0121.rgb sd_fx29.0134.rgb sd_fx29.0146.rgb
>sd_fx29.0110.rgb sd_fx29.0123.rgb sd_fx29.0135.rgb sd_fx29.0147.rgb
>sd_fx29.0111.rgb sd_fx29.0124.rgb sd_fx29.0136.rgb strange.xml

>\>lss  
>1 alpha.txt  
>1 elem.info  
>46 sd_fx29.%04d.rgb 101-121,123-147  
>1 strange.xml  