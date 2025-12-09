const form = document.getElementById('regForm');
    const pwd = document.getElementById('password');
    const confirmPwd = document.getElementById('confirmPassword');
    const pwdMeter = document.getElementById('pwdMeter');
    const msg = document.getElementById('formMessage');

    function setError(id, text){ document.getElementById('err-'+id).textContent = text || ''; }

    function passwordScore(s){
      let score = 0;
      if(s.length >= 8) score++;
      if(/[a-z]/.test(s) && /[A-Z]/.test(s)) score++;
      if(/[0-9]/.test(s)) score++;
      if(/[^A-Za-z0-9]/.test(s)) score++;
      return score; // 0..4
    }

    pwd.addEventListener('input', ()=>{
      const s = passwordScore(pwd.value);
      const pct = (s/4)*100;
      pwdMeter.style.width = pct + '%';
      // change meter color by setting gradient stops via style (simple)
      if(pct < 34) pwdMeter.style.background = 'linear-gradient(90deg,#f97316,#ef4444)';
      else if(pct < 67) pwdMeter.style.background = 'linear-gradient(90deg,#f59e0b,#f97316)';
      else pwdMeter.style.background = 'linear-gradient(90deg,#10b981,#059669)';
    });

    form.addEventListener('submit', (e)=>{
      e.preventDefault();
      // clear previous errors
      ['firstName','lastName','email','password','confirmPassword','phone','dob','terms'].forEach(id=>setError(id,''));
      msg.textContent = '';

      let valid = true;
      const firstName = form.firstName.value.trim();
      const lastName = form.lastName.value.trim();
      const email = form.email.value.trim();
      const password = form.password.value;
      const confirm = form.confirmPassword.value;
      const terms = form.terms.checked;

      if(firstName.length < 2){ setError('firstName','Enter your first name (min 2 chars)'); valid=false }
      if(lastName.length < 2){ setError('lastName','Enter your last name (min 2 chars)'); valid=false }
      if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)){ setError('email','Enter a valid email address'); valid=false }
      if(password.length < 8){ setError('password','Password must be at least 8 characters'); valid=false }
      if(password !== confirm){ setError('confirmPassword','Passwords do not match'); valid=false }
      if(!terms){ setError('terms','You must agree to the terms'); valid=false }

      if(!valid){ msg.textContent = 'Please fix the errors above.'; return }

      // simulate submission result
      document.getElementById('submitBtn').disabled = true;
      msg.textContent = 'Creating account...';

      // In real app, replace with fetch() call to your backend API.
      setTimeout(()=>{
        msg.textContent = '';
        document.getElementById('submitBtn').disabled = false;
        msg.className = 'success';
        msg.textContent = 'Account created — check your email to verify.';
        form.reset();
        pwdMeter.style.width = '0%';
      }, 900);
    });