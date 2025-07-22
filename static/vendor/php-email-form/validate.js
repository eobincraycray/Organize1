/**
* PHP Email Form Validation - v3.10
* URL: https://bootstrapmade.com/php-email-form/
* Author: BootstrapMade.com
*/
/**
(function () {
  "use strict";

  let forms = document.querySelectorAll('.php-email-form');

  forms.forEach(function (e) {
    e.addEventListener('submit', function (event) {
      event.preventDefault(); // Impede o envio tradicional do formulário

      let thisForm = this;
      let action = thisForm.getAttribute('action');
      
      // Exibe a animação de carregamento
      thisForm.querySelector('.loading').classList.remove('d-none');
      thisForm.querySelector('.error-message').classList.add('d-none');
      thisForm.querySelector('.sent-message').classList.add('d-none');

      let formData = new FormData(thisForm);

      // Envia a requisição AJAX para o Django
      fetch(action, {
        method: 'POST',
        body: formData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': thisForm.querySelector('[name="csrfmiddlewaretoken"]').value  // CSRF token necessário para Django
        }
      })
      .then(response => {
        if (response.ok) {
          return response.json(); // Espera que o Django retorne um JSON
        } else {
          throw new Error(`${response.status} ${response.statusText} ${response.url}`);
        }
      })
      .then(data => {
        thisForm.querySelector('.loading').classList.add('d-none');

        if (data.success) {
          thisForm.querySelector('.sent-message').classList.remove('d-none');
          thisForm.reset();
        } else {
          displayError(thisForm, data.message);
        }
      })
      .catch(error => {
        displayError(thisForm, error.message);
      });
    });
  });

  function displayError(thisForm, error) {
    thisForm.querySelector('.loading').classList.add('d-none');
    thisForm.querySelector('.error-message').innerHTML = error;
    thisForm.querySelector('.error-message').classList.remove('d-none');
  }

})();
*/