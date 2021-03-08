var pDesk;
var isSliced = false;




function lload() {
  
  fetch('/ret-pastors-desk/', {method: 'GET'})
  .then(res => res.text())
  .then(restwo => {
    pDesk = restwo;
    document.getElementById("pastors-desk2").innerText = restwo.slice(0, 250) + '...';
    btnText.innerHTML = "Read more";
  })
  .catch(err => console.log(err)) 
}
  lload();


 
  function myFunctionTwo() {    
    // var dots = document.getElementById("dots");
    let pastorsDesk = document.getElementById("pastors-desk2");
    let btnText = document.getElementById("myBtn2");
    // console.log(pastorsDesk.innerText);
    // return 0;
    
    if (isSliced) {
      pastorsDesk.innerText = pDesk.slice(0, 250) + '...';
      btnText.innerHTML = "Read more";
      isSliced = false;
      // moreText.style.display = "none";
      
    } else {
      pastorsDesk.innerText = pDesk;
      btnText.innerHTML = "Read less";
      isSliced = true;
      // moreText.style.display = "inline";
    }
  }

  function doIt() {
    console.log(pDesk);
    let pastorsDesk = document.getElementById("pastors-desk2");
    let btnText = document.getElementById("myBtn2");
      pastorsDesk.innerText = pDesk.slice(0, 40) + '...';
        btnText.innerHTML = "Read more";
        isSliced = false;
        
  }
  doIt(); 