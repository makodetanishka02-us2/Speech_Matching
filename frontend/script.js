const audioA = document.getElementById("audioA");
const audioB = document.getElementById("audioB");

const textA = document.getElementById("textA");
const textB = document.getElementById("textB");

const compareButton = document.getElementById("compareButton");

const result = document.getElementById("result");

let fileA = null;
let fileB = null;


/* =========================
   FILE A
========================= */

audioA.addEventListener("change", function () {

    if (this.files.length > 0) {

        fileA = this.files[0];

        textA.textContent = fileA.name;

        checkFiles();
    }

});


/* =========================
   FILE B
========================= */

audioB.addEventListener("change", function () {

    if (this.files.length > 0) {

        fileB = this.files[0];

        textB.textContent = fileB.name;

        checkFiles();
    }

});


/* =========================
   CHECK BOTH FILES
========================= */

function checkFiles() {

    if (fileA && fileB) {

        compareButton.disabled = false;

    } else {

        compareButton.disabled = true;

    }

}


/* =========================
   DISPLAY FINGERPRINT
========================= */

function displayFingerprintCharacters(id, fingerprint) {

    const container = document.getElementById(id);

    container.innerHTML = "";

    for (const character of fingerprint) {

        const span = document.createElement("span");

        span.textContent = character;

        container.appendChild(span);
    }

}


/* =========================
   COMPARE
========================= */

compareButton.addEventListener("click", async function () {

    if (!fileA || !fileB) {
        return;
    }

    compareButton.disabled = true;

    compareButton.textContent = "⏳ Comparing...";


    const formData = new FormData();

    formData.append("audioA", fileA);
    formData.append("audioB", fileB);


    try {

        const response = await fetch(
       "https://speech-matching.onrender.com/compare",
            {
                method: "POST",
                body: formData
            }
        );


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.error || "Comparison failed."
            );

        }


        /* =========================
           FINGERPRINT RESULTS
        ========================= */

        document.getElementById("fingerprintA").textContent =
            data.fingerprintA;

        document.getElementById("fingerprintB").textContent =
            data.fingerprintB;


        /* Individual characters */

        displayFingerprintCharacters(
            "fingerprintCharsA",
            data.fingerprintA
        );

        displayFingerprintCharacters(
            "fingerprintCharsB",
            data.fingerprintB
        );


        /* =========================
           LCS RESULT
        ========================= */

        document.getElementById("lcsLength").textContent =
            data.lcsLength;


        /* =========================
           SIMILARITY
        ========================= */

        document.getElementById("similarity").textContent =
            data.similarity + "%";


        /* =========================
           SHOW RESULT
        ========================= */

        result.classList.remove("hidden");


        result.scrollIntoView({
            behavior: "smooth"
        });


    } catch (error) {

        alert(
            "Error connecting to backend:\n" +
            error.message
        );

        console.error(error);

    }


    compareButton.disabled = false;

    compareButton.textContent = " Compare Fingerprints";

});