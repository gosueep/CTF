window.addEventListener('load', () => {
    document.querySelector('form').addEventListener('submit', async (event) => {
      event.preventDefault();
  
      if (!window.PublicKeyCredential) {
        window.alert('Use a modern browser that supports WebAuthn');
        return;
      }
  
      try {
        const form = new FormData(event.target);
  
        const response = await fetch('/signup/public-key/challenge', {
          method : 'POST',
          headers : {
            Accept : 'application/json',
            'Content-Type' : 'application/json',
          },
          body : JSON.stringify({ name : form.get('name'), username : form.get('username') }),
        });
  
        const json = await response.json();
        if (response.status >= 400) {
          window.alert(json.message);
          return;
        }
  
        // https://chromium.googlesource.com/chromium/src/+/master/content/browser/webauth/uv_preferred.md
        const credential = await navigator.credentials.create({
          publicKey : {
            rp : {
              name : 'CityInTheCloud',
            },
            user : {
              id : (new TextEncoder()).encode(json.user.name),
              name : json.user.name,
              displayName : json.user.name,
            },
            challenge : base64url.decode(json.challenge),
            pubKeyCredParams : [
              {
                type : 'public-key',
                alg : -7, // "ES256" IANA COSE Algorithms registry
              },
            ],
            // attestation: 'none',
            authenticatorSelection : {
              userVerification : 'discouraged',
              // authenticatorAttachment: "platform",
              residentKey : 'required',
            },
          },
        });
  
        const body = {
          response : {
            clientDataJSON : base64url.encode(credential.response.clientDataJSON),
            attestationObject : base64url.encode(credential.response.attestationObject),
          },
        };
        if (credential.response.getTransports) {
          body.response.transports = credential.response.getTransports();
        }
  
        const loginResponse = await fetch('/login/public-key', {
          method : 'POST',
          headers : {
            'Content-Type' : 'application/json',
            Accept : 'application/json',
          },
          body : JSON.stringify(body),
        });
  
        const { location } = await loginResponse.json();
        window.location.href = location;
      } catch (err) {
        window.alert(err.message);
        console.error(err);
      }
    });
  });
  