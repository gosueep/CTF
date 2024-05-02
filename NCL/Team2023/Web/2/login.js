window.addEventListener('load', () => {
  document.getElementById('siw-public-key').addEventListener('click', async (event) => {
    event.preventDefault();

    if (!window.PublicKeyCredential) {
      window.alert('Use a modern browser that supports WebAuthn');
      return;
    }

    try {
      const response = await fetch('/login/public-key/challenge', {
        method : 'POST',
        headers : {
          Accept : 'application/json',
        },
      });
      const json = await response.json();
      if (response.status >= 400) {
        window.alert(json.message);
        return;
      }
      const credential = await navigator.credentials.get({
        publicKey : {
          challenge : base64url.decode(json.challenge),
        },
      });
      const body = {
        id : credential.id,
        response : {
          clientDataJSON : base64url.encode(credential.response.clientDataJSON),
          authenticatorData : base64url.encode(credential.response.authenticatorData),
          signature : base64url.encode(credential.response.signature),
          userHandle : credential.response.userHandle ? base64url.encode(credential.response.userHandle) : null,
        },
      };
      if (credential.authenticatorAttachment) {
        body.authenticatorAttachment = credential.authenticatorAttachment;
      }

      const pubKeyResponse = await fetch('/login/public-key', {
        method : 'POST',
        headers : {
          'Content-Type' : 'application/json',
          Accept : 'application/json',
        },
        body : JSON.stringify(body),
      });
      const { location } = await pubKeyResponse.json();
      window.location.href = location;
    } catch (err) {
      window.alert(err.message);
      console.error(err);
    }
  });
});
