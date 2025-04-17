document.getElementById('signupForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // Vérifie si les mots de passe correspondent
    if (password !== confirmPassword) {
        alert('Les mots de passe ne correspondent pas.');
        return;
    }

    // Vérifie les critères du mot de passe
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordRegex.test(password)) {
        alert('Le mot de passe ne respecte pas les critères de sécurité :\n- Au moins 8 caractères\n- Une lettre majuscule\n- Une lettre minuscule\n- Un chiffre\n- Un caractère spécial');
        return;
    }

    // Si tout est valide, soumettre le formulaire
    this.submit();
});