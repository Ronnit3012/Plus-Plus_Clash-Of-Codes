var slideIndex = 1;

var myTimer;

var slideshowContainer;

window.addEventListener("load",function() {
    showSlides(slideIndex);
    myTimer = setInterval(function(){plusSlides(1)}, 4000);
  
    //COMMENT OUT THE LINE BELOW TO KEEP ARROWS PART OF MOUSEENTER PAUSE/RESUME
    slideshowContainer = document.getElementsByClassName('slideshow-inner')[0];
  
    //UNCOMMENT OUT THE LINE BELOW TO KEEP ARROWS PART OF MOUSEENTER PAUSE/RESUME
    // slideshowContainer = document.getElementsByClassName('slideshow-container')[0];
  
    slideshowContainer.addEventListener('mouseenter', pause)
    slideshowContainer.addEventListener('mouseleave', resume)
})

// NEXT AND PREVIOUS CONTROL
function plusSlides(n){
  clearInterval(myTimer);
  if (n < 0){
    showSlides(slideIndex -= 1);
  } else {
   showSlides(slideIndex += 1); 
  }
  
  //COMMENT OUT THE LINES BELOW TO KEEP ARROWS PART OF MOUSEENTER PAUSE/RESUME
  
  if (n === -1){
    myTimer = setInterval(function(){plusSlides(n + 2)}, 4000);
  } else {
    myTimer = setInterval(function(){plusSlides(n + 1)}, 4000);
  }
}

//Controls the current slide and resets interval if needed
function currentSlide(n){
  clearInterval(myTimer);
  myTimer = setInterval(function(){plusSlides(n + 1)}, 4000);
  showSlides(slideIndex = n);
}

function showSlides(n){
  var i;
  var slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}

pause = () => {
  clearInterval(myTimer);
}

resume = () =>{
  clearInterval(myTimer);
  myTimer = setInterval(function(){plusSlides(slideIndex)}, 4000);
}

const getStartedTop = document.getElementById('get-started-top');
const getStartedMid = document.getElementById('get-started-mid');

getStartedTop.addEventListener('click', (e) => {
  e.preventDefault();
  var element = document.getElementById("main");
  element.scrollIntoView();
})
getStartedMid.addEventListener('click', (e) => {
  e.preventDefault();
  var element = document.getElementById("main");
  element.scrollIntoView();
})

const originalImage = document.getElementById('originalImg');
const annotatedImage = document.getElementById('annotatedImg');
const sampleOg = document.getElementById('sampleOg');
const sampleAn = document.getElementById('sampleAn');
const genderSpan = document.getElementById('gender');
const ageSpan = document.getElementById('age');

document.getElementById('image-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const baseUrl = window.location.origin;
  const formData = new FormData(e.target);
  const formProps = Object.fromEntries(formData);

  try {
    const res = await axios.post(`${baseUrl}/api/v1/analysis`, formProps);
    console.log(res.data);
    // const { originalImg, annotatedImg, isReal, gender, genderPreds } = res.data;

    // if(res.status === 200) {
    //   if(isReal) {
    //     sampleOg.style.display = 'none';
    //     sampleAn.style.display = 'none';
    //     originalImage.src = originalImg;
    //     annotatedImage.src = annotatedImg;
    //     originalImage.style.display = 'block';
    //     annotatedImage.style.display = 'block';
    //     genderSpan.innerHTML = gender;
    //   }
    // }



  } catch (error) {
    console.log(error.message);
  }
});