/*
Core logic/payment flow comes from :
https://stripe.com/docs/payments/accept-a-payment

Css from:
https://stripe.com/docs/stripe-js
*/

var stripePublicKey  = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret  = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var card = elements.create('card');

var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

card.mount('#card-element');

// Handle realtime validation error on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit 
// Create a token or display an error when the form is submitted.
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    card.update({ 'disabled', true});
    $('#submit-button').attr('disabled', true)
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }

//   stripe.createToken(card).then(function(result) {
    }).then(function(result) {
    if (result.error) {
      // Inform the customer that there was an error.
    //   var errorElement = document.getElementById('card-errors');
    //   errorElement.textContent = result.error.message;
    var errorDiv = document.getElementById('card-errors');
    var html = `
        <span class="icon" role="alert">
        <i class="fas fa-times"></i>
        </span>
        <span>${result.error.message}</span>`;
    $(errorDiv).html(html);
    card.update({ 'disabled': false});
    $('#submit-button').attr('disabled', false);
    } else {
      // Send the token to your server.
    //   stripeTokenHandler(result.token);
      if (result.paymentIntent.status === 'succeeded') {
        form.submit();
    }
  });
});
