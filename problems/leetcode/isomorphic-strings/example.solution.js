function isIsomorphic(s, t) {
  const obj = {};

  for (let i = 0; i < s.length; i++) {
    console.log(obj['s' + s[i]]);
    if (!obj['s' + s[i]])
      obj['s' + s[i]] = t[i];
    if (!obj['t' + t[i]])
      obj['t' + t[i]] = s[i];
    if (t[i] != obj['s' + s[i]] || s[i] != obj['t' + t[i]])
      return false;
  }
  return true;
}

const t = 'egg';
const s = 'add';
const res = isIsomorphic(t, s);
console.log(res);
