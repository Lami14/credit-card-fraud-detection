document.getElementById('fraudForm').addEventListener('submit', function(e){
    e.preventDefault();
    const data = {
        amount: parseFloat(document.getElementById('amount').value),
        location: document.getElementById('location').value,
        card_type: document.getElementById('card_type').value,
        merchant_category: document.getElementById('merchant_category').value
    };
    fetch('/predict', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result').innerText = `Transaction Status: ${result.transaction_status}`;
    })
    .catch(error => console.error(error));
});
