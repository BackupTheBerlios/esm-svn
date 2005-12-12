function showtip(current,e,text)
// show a tool tip, e.g. usually for mouse over effects
//
// for example:  onMouseOver="showtip(this,event,'This is a tool tip')"
{
  if (document.all) {
    thetitle=text.split('<BR>')
    if (thetitle.length>1) {
        thetitles=''
        for (i=0;i<thetitle.length;i++)
          thetitles+=thetitle[i]
        current.title=thetitles
    } else
        current.title=text
  } else
    if (document.layers){
      document.tooltip.document.write('<layer bgColor="white" style="border:1px solid black;">'+text+'<\/layer>')
      document.tooltip.document.close()
      document.tooltip.left=e.pageX+5
      document.tooltip.top=e.pageY+5
      document.tooltip.visibility="show"
    }
}

function hidetip()
// hide the tooltip
//
// for example:  onMouseOut="hidetip()"
{
    if (document.layers)
        document.tooltip.visibility="hidden"
}
