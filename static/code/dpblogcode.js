window.addEventListener('scroll', () => {
    const header = document.getElementById('main-header');
    if (window.scrollY === 0) {
      header.classList.remove('scrolled');
    } else {
      header.classList.add('scrolled');
    }
  });

const infoContainer = document.getElementById("info");

const frameContainer = document.getElementById("frame");

        function showInfo(objectId) {
            const objectInfo = getObjectInfo(objectId);
            let imgSrc = null;
            if (objectInfo) {

            const allImages = document.querySelectorAll('.object-container img');
                allImages.forEach(image => {
                        if(image.id == 'career'){
                            image.src = "{% static 'portfolio/carreira-notSelected.png' %}";
                        } else if(image.id == 'cumputing'){
                            image.src = "{% static 'portfolio/uni-notSelected.png' %}";
                        } else if(image.id == 'editor'){
                            image.src = "{% static 'portfolio/editor-notSelected.png' %}";
                        } else if(image.id == 'skills'){
                            image.src = "{% static 'portfolio/skills-notSelected.png' %}";
                        }
                });

                if(objectId == 'object1'){
                    const objectImageElement = document.getElementById('career');
                    imgSrc = "{% static 'portfolio/carreira.png' %}";
                    objectImageElement.src = imgSrc;
                    frame.src = `../../assets/templates/aboutPages/career.html`;
                } else if(objectId == 'object2'){
                    const objectImageElement = document.getElementById('cumputing');
                    imgSrc = "{% static 'portfolio/uni.png' %}";
                    objectImageElement.src = imgSrc;
                    frame.src = `../../assets/templates/aboutPages/uni.html`;
                } else if(objectId == 'object3'){
                    const objectImageElement = document.getElementById('editor');
                    imgSrc = "{% static 'portfolio/editor.png' %}";
                    objectImageElement.src = imgSrc;
                } else if(objectId == 'object4'){
                    const objectImageElement = document.getElementById('skills');
                    imgSrc = "{% static 'portfolio/skills.png' %}";
                    objectImageElement.src = imgSrc;
                }

                var iframe = document.getElementById('info');
                iframe.style.display = 'block';
                iframe.scrollIntoView({ behavior: 'smooth' });



            }


        }

        const birthday = '1998-08-29';

        function calculateAge(birthdate) {
            const birthdateArray = birthdate.split('-');
            const birthYear = parseInt(birthdateArray[0]);
            const birthMonth = parseInt(birthdateArray[1]);
            const birthDay = parseInt(birthdateArray[2]);

            const today = new Date();
            const currentYear = today.getFullYear();
            const currentMonth = today.getMonth() + 1; // Months are 0-indexed
            const currentDay = today.getDate();

            let age = currentYear - birthYear;


            if (currentMonth < birthMonth || (currentMonth === birthMonth && currentDay < birthDay)) {
                age--;
            }

            return age;
        }

        const age = calculateAge(birthday);
        const dynamicParagraph = document.getElementById('age-paragraph');
        dynamicParagraph.textContent = `Hello, thank you for visiting my website! My name is Tomé Roque, and I am ${age} years old.`;