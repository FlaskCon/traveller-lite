(function(){const t=document.createElement("link").relList;if(t&&t.supports&&t.supports("modulepreload"))return;for(const l of document.querySelectorAll('link[rel="modulepreload"]'))s(l);new MutationObserver(l=>{for(const r of l)if(r.type==="childList")for(const o of r.addedNodes)o.tagName==="LINK"&&o.rel==="modulepreload"&&s(o)}).observe(document,{childList:!0,subtree:!0});function n(l){const r={};return l.integrity&&(r.integrity=l.integrity),l.referrerPolicy&&(r.referrerPolicy=l.referrerPolicy),l.crossOrigin==="use-credentials"?r.credentials="include":l.crossOrigin==="anonymous"?r.credentials="omit":r.credentials="same-origin",r}function s(l){if(l.ep)return;l.ep=!0;const r=n(l);fetch(l.href,r)}})();const z=(e,t)=>e===t,k={equals:z};let R=j;const g=1,U=2,D={owned:null,cleanups:null,context:null,owner:null};var d=null;let P=null,K=null,c=null,u=null,y=null,F=0;function J(e,t){const n=c,s=d,l=e.length===0,r=t===void 0?s:t,o=l?D:{owned:null,cleanups:null,context:r?r.context:null,owner:r},i=l?e:()=>e(()=>m(()=>V(o)));d=o,c=null;try{return S(i,!0)}finally{c=n,d=s}}function M(e,t){t=t?Object.assign({},k,t):k;const n={value:e,observers:null,observerSlots:null,comparator:t.equals||void 0},s=l=>(typeof l=="function"&&(l=l(n.value)),Q(n,l));return[L.bind(n),s]}function T(e,t,n){const s=B(e,t,!1,g);E(s)}function _(e,t,n){R=ne;const s=B(e,t,!1,g);(!n||!n.render)&&(s.user=!0),y?y.push(s):E(s)}function X(e,t,n){n=n?Object.assign({},k,n):k;const s=B(e,t,!0,0);return s.observers=null,s.observerSlots=null,s.comparator=n.equals||void 0,E(s),L.bind(s)}function m(e){if(c===null)return e();const t=c;c=null;try{return e()}finally{c=t}}function $(e){_(()=>m(e))}function L(){if(this.sources&&this.state)if(this.state===g)E(this);else{const e=u;u=null,S(()=>I(this),!1),u=e}if(c){const e=this.observers?this.observers.length:0;c.sources?(c.sources.push(this),c.sourceSlots.push(e)):(c.sources=[this],c.sourceSlots=[e]),this.observers?(this.observers.push(c),this.observerSlots.push(c.sources.length-1)):(this.observers=[c],this.observerSlots=[c.sources.length-1])}return this.value}function Q(e,t,n){let s=e.value;return(!e.comparator||!e.comparator(s,t))&&(e.value=t,e.observers&&e.observers.length&&S(()=>{for(let l=0;l<e.observers.length;l+=1){const r=e.observers[l],o=P&&P.running;o&&P.disposed.has(r),(o?!r.tState:!r.state)&&(r.pure?u.push(r):y.push(r),r.observers&&G(r)),o||(r.state=g)}if(u.length>1e6)throw u=[],new Error},!1)),t}function E(e){if(!e.fn)return;V(e);const t=F;ee(e,e.value,t)}function ee(e,t,n){let s;const l=d,r=c;c=d=e;try{s=e.fn(t)}catch(o){return e.pure&&(e.state=g,e.owned&&e.owned.forEach(V),e.owned=null),e.updatedAt=n+1,O(o)}finally{c=r,d=l}(!e.updatedAt||e.updatedAt<=n)&&(e.updatedAt!=null&&"observers"in e?Q(e,s):e.value=s,e.updatedAt=n)}function B(e,t,n,s=g,l){const r={fn:e,state:s,updatedAt:null,owned:null,sources:null,sourceSlots:null,cleanups:null,value:t,owner:d,context:d?d.context:null,pure:n};return d===null||d!==D&&(d.owned?d.owned.push(r):d.owned=[r]),r}function Y(e){if(e.state===0)return;if(e.state===U)return I(e);if(e.suspense&&m(e.suspense.inFallback))return e.suspense.effects.push(e);const t=[e];for(;(e=e.owner)&&(!e.updatedAt||e.updatedAt<F);)e.state&&t.push(e);for(let n=t.length-1;n>=0;n--)if(e=t[n],e.state===g)E(e);else if(e.state===U){const s=u;u=null,S(()=>I(e,t[0]),!1),u=s}}function S(e,t){if(u)return e();let n=!1;t||(u=[]),y?n=!0:y=[],F++;try{const s=e();return te(n),s}catch(s){n||(y=null),u=null,O(s)}}function te(e){if(u&&(j(u),u=null),e)return;const t=y;y=null,t.length&&S(()=>R(t),!1)}function j(e){for(let t=0;t<e.length;t++)Y(e[t])}function ne(e){let t,n=0;for(t=0;t<e.length;t++){const s=e[t];s.user?e[n++]=s:Y(s)}for(t=0;t<n;t++)Y(e[t])}function I(e,t){e.state=0;for(let n=0;n<e.sources.length;n+=1){const s=e.sources[n];if(s.sources){const l=s.state;l===g?s!==t&&(!s.updatedAt||s.updatedAt<F)&&Y(s):l===U&&I(s,t)}}}function G(e){for(let t=0;t<e.observers.length;t+=1){const n=e.observers[t];n.state||(n.state=U,n.pure?u.push(n):y.push(n),n.observers&&G(n))}}function V(e){let t;if(e.sources)for(;e.sources.length;){const n=e.sources.pop(),s=e.sourceSlots.pop(),l=n.observers;if(l&&l.length){const r=l.pop(),o=n.observerSlots.pop();s<l.length&&(r.sourceSlots[o]=s,l[s]=r,n.observerSlots[s]=o)}}if(e.owned){for(t=e.owned.length-1;t>=0;t--)V(e.owned[t]);e.owned=null}if(e.cleanups){for(t=e.cleanups.length-1;t>=0;t--)e.cleanups[t]();e.cleanups=null}e.state=0}function se(e){return e instanceof Error?e:new Error(typeof e=="string"?e:"Unknown error",{cause:e})}function O(e,t=d){throw se(e)}let le=!1;function ie(e,t){return m(()=>e(t||{}))}const re=e=>`Stale read from <${e}>.`;function oe(e){const t=e.keyed,n=X(()=>e.when,void 0,{equals:(s,l)=>t?s===l:!s==!l});return X(()=>{const s=n();if(s){const l=e.children;return typeof l=="function"&&l.length>0?m(()=>l(t?s:()=>{if(!m(n))throw re("Show");return e.when})):l}return e.fallback},void 0,void 0)}function ce(e,t,n){let s=n.length,l=t.length,r=s,o=0,i=0,f=t[l-1].nextSibling,h=null;for(;o<l||i<r;){if(t[o]===n[i]){o++,i++;continue}for(;t[l-1]===n[r-1];)l--,r--;if(l===o){const a=r<s?i?n[i-1].nextSibling:n[r-i]:f;for(;i<r;)e.insertBefore(n[i++],a)}else if(r===i)for(;o<l;)(!h||!h.has(t[o]))&&t[o].remove(),o++;else if(t[o]===n[r-1]&&n[i]===t[l-1]){const a=t[--l].nextSibling;e.insertBefore(n[i++],t[o++].nextSibling),e.insertBefore(n[--r],a),t[l]=n[r]}else{if(!h){h=new Map;let p=i;for(;p<r;)h.set(n[p],p++)}const a=h.get(t[o]);if(a!=null)if(i<a&&a<r){let p=o,b=1,C;for(;++p<l&&p<r&&!((C=h.get(t[p]))==null||C!==a+b);)b++;if(b>a-i){const H=t[o];for(;i<a;)e.insertBefore(n[i++],H)}else e.replaceChild(n[i++],t[o++])}else o++;else t[o++].remove()}}}function fe(e,t,n,s={}){let l;return J(r=>{l=r,t===document?e():v(t,e(),t.firstChild?null:void 0,n)},s.owner),()=>{l(),t.textContent=""}}function w(e,t,n){let s;const l=()=>{const o=document.createElement("template");return o.innerHTML=e,n?o.content.firstChild.firstChild:o.content.firstChild},r=t?()=>m(()=>document.importNode(s||(s=l()),!0)):()=>(s||(s=l())).cloneNode(!0);return r.cloneNode=r,r}function ue(e,t,n){n==null?e.removeAttribute(t):e.setAttribute(t,n)}function v(e,t,n,s){if(n!==void 0&&!s&&(s=[]),typeof t!="function")return q(e,t,s,n);T(l=>q(e,t(),l,n),s)}function q(e,t,n,s,l){for(;typeof n=="function";)n=n();if(t===n)return n;const r=typeof t,o=s!==void 0;if(e=o&&n[0]&&n[0].parentNode||e,r==="string"||r==="number")if(r==="number"&&(t=t.toString()),o){let i=n[0];i&&i.nodeType===3?i.data!==t&&(i.data=t):i=document.createTextNode(t),n=A(e,n,s,i)}else n!==""&&typeof n=="string"?n=e.firstChild.data=t:n=e.textContent=t;else if(t==null||r==="boolean")n=A(e,n,s);else{if(r==="function")return T(()=>{let i=t();for(;typeof i=="function";)i=i();n=q(e,i,n,s)}),()=>n;if(Array.isArray(t)){const i=[],f=n&&Array.isArray(n);if(W(i,t,n,l))return T(()=>n=q(e,i,n,s,!0)),()=>n;if(i.length===0){if(n=A(e,n,s),o)return n}else f?n.length===0?Z(e,i,s):ce(e,n,i):(n&&A(e),Z(e,i));n=i}else if(t.nodeType){if(Array.isArray(n)){if(o)return n=A(e,n,s,t);A(e,n,null,t)}else n==null||n===""||!e.firstChild?e.appendChild(t):e.replaceChild(t,e.firstChild);n=t}}return n}function W(e,t,n,s){let l=!1;for(let r=0,o=t.length;r<o;r++){let i=t[r],f=n&&n[e.length],h;if(!(i==null||i===!0||i===!1))if((h=typeof i)=="object"&&i.nodeType)e.push(i);else if(Array.isArray(i))l=W(e,i,f)||l;else if(h==="function")if(s){for(;typeof i=="function";)i=i();l=W(e,Array.isArray(i)?i:[i],Array.isArray(f)?f:[f])||l}else e.push(i),l=!0;else{const a=String(i);f&&f.nodeType===3&&f.data===a?e.push(f):e.push(document.createTextNode(a))}}return l}function Z(e,t,n=null){for(let s=0,l=t.length;s<l;s++)e.insertBefore(t[s],n)}function A(e,t,n,s){if(n===void 0)return e.textContent="";const l=s||document.createTextNode("");if(t.length){let r=!1;for(let o=t.length-1;o>=0;o--){const i=t[o];if(l!==i){const f=i.parentNode===e;!r&&!o?f?e.replaceChild(l,i):e.insertBefore(l,n):f&&i.remove()}else r=!0}}else e.insertBefore(l,n);return[l]}const ae="/__vt/vite_2024_frontend/flaskcon-2024-animated-c40df053.gif",N="data:image/png;base64,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";var de=w("<h2 class=mb-2>Call for proposals are now live!"),he=w("<p>Call for proposals will end on "),pe=w(`<section><div class=hero><div class=hero-overlay><img alt="FlaskCon 2024 Logo."></div></div><section class=container><h1 class="text-center my-14">FlaskCon 2024 will be happening Friday, May 17 inside PyCon US 2024.</h1></section><section class="container mb-14"><div class="mt-5 mb-10 text-center"></div><div class="flex justify-center w-full"></div></section><section class=container><h2 class=my-5>Proposal Ideas!</h2><p>If you are a developer who uses or contributes to Flask, Click, Jinja, or other parts of Pallets, designers who work with them, or sysadmins who administer them, here are some talk ideas to consider:</p><ul><li>HTMX</li><li>WSGI and ASGI</li><li>Accessibility</li><li>Performance</li><li>Case Studies</li><li>Your experience as a newbie</li></ul></section><section class=container><h2 class=my-5>Speaking Experience</h2><ul><li>We are focused on accepting lightning talks this year, typically 5 - 15 mins.</li><li>If your talk is accepted and you haven't secured a PyCon 2024 ticket yet, you'll need to sign up to acquire one for entry to the venue. You can register for a ticket by following <a href=https://us.pycon.org/2024/registration/register>this link here</a></li></ul></section><section class=container><h2 class=my-5>The Current Schedule (may change)</h2><table><thead><tr><th>Time</th><th>Event</th></tr></thead><tbody><tr><td>11:00 - 11:15</td><td>Intro from David Lord</td></tr><tr><td>11:15 - 11:40</td><td>State of Pallets</td></tr><tr><td>11:40 - 12:00</td><td>Q&A</td></tr><tr><td>12:00 - 13:00</td><td>Lightning Talks</td></tr><tr><td>13:00 - 14:00</td><td>Lunch</td></tr><tr><td>14:00 - 14:25</td><td>Being a Better Community</td></tr><tr><td>14:30 - 15:30</td><td>Lightning Talks</td></tr><tr><td>15:40 - 16:00</td><td>Becoming a Contributor</td></tr><tr><td>16:00 - 16:30</td><td>Break</td></tr><tr><td>16:30 - 17:30</td><td>Lightning Talks</td></tr><tr><td>17:30 - 17:40</td><td>Future of Pallets</td></tr><tr><td>17:40 - 18:00</td><td>Panel Q&A</td></tr><tr><td>18:00 - 19:00</td><td>General Mixer?</td></tr></tbody></table></section><section class="container text-center"><p class=text-sm>Copyright &copy; 2024 FlaskCon, A PSF-registered trademark owned by Pallets.`),ye=w("<h2>Call for proposals have ended."),ge=w('<div class="flex flex-col gap-2 text-center"><a class=btn href=https://flaskcon.com/account>Go to my account'),me=w('<div class="flex flex-col gap-2 text-center"><a class=btn href=https://flaskcon.com/signup>Signup To Join In</a><a href=https://flaskcon.com/login>...or login here');function Ae(){const[e,t]=M(!1),[n,s]=M({}),l="/";function r(){fetch(l+"api/logged-in",{method:"GET",credentials:"include",headers:{"Content-Type":"application/json"}}).then(i=>i.json()).then(i=>{i.logged_in&&t(!0)})}function o(){fetch(l+"api/conference/2024",{method:"GET",credentials:"include",headers:{"Content-Type":"application/json"}}).then(i=>i.json()).then(i=>{s(i)})}return $(()=>{r(),o()}),(()=>{var i=pe(),f=i.firstChild,h=f.firstChild,a=h.firstChild,p=f.nextSibling,b=p.nextSibling,C=b.firstChild,H=C.nextSibling;return`url(${N}) repeat-x bottom`!=null?h.style.setProperty("background",`url(${N}) repeat-x bottom`):h.style.removeProperty("background"),ue(a,"src",ae),v(C,ie(oe,{get when(){return n().call_for_proposals_days_left>-1},get fallback(){return ye()},get children(){return[de(),(()=>{var x=he();return x.firstChild,v(x,()=>n().call_for_proposals_end_date,null),x})()]}})),v(H,(()=>{var x=X(()=>!!e());return()=>x()?ge():me()})()),i})()}const we=document.getElementById("root");fe(()=>Ae,we);