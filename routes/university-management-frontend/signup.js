document.addEventListener('DOMContentLoaded', () => {
    const signupForm = document.getElementById('signup-form');
  
    signupForm.addEventListener('submit', async (e) => {
      e.preventDefault();
  
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const password = document.getElementById('password').value.trim();
      const role = document.getElementById('role').value; // Optional: use if role dropdown exists
  
      try {
        const res = await fetch('http://localhost:3000/api/auth/signup', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name, email, password, role })
        });
  
        const data = await res.json();
  
        if (res.ok && data.message === 'User created successfully') {
          alert('Signup successful! Please login to continue.');
          window.location.href = 'login.html'; // ✅ Redirect to login page
        } else {
          alert(data.message || 'Signup failed');
        }
      } catch (err) {
        console.error('Signup error:', err);
        alert('An error occurred during signup');
      }
    });
  });
  