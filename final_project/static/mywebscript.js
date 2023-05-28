let translateToFrench = () => {
  textToTranslate = document.getElementById("textToTranslate").value;

  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("translated_text").innerHTML = JSON.parse(
        xhttp.responseText
      );
    }
  };
  xhttp.open(
    "GET",
    "englishToFrench?textToTranslate" + "=" + textToTranslate,
    true
  );
  xhttp.send();
};

let translateToEnglish = () => {
  textToTranslate = document.getElementById("textToTranslate").value;

  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("translated_text").innerHTML = JSON.parse(
        xhttp.responseText
      );
    }
  };
  xhttp.open(
    "GET",
    "frenchToEnglish?textToTranslate" + "=" + textToTranslate,
    true
  );
  xhttp.send();
};
