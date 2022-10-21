(function changeColor() {
    let color = document.getElementsByTagName('body')[0].className
    if (color === 'dark') {
      document.getElementsByTagName('body')[0].className = ""
    } else {
      document.getElementsByTagName('body')[0].className = "dark"
    }
  })()