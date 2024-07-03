// @todo learn mechanism of hash tables
function isIsomorphic(s: string, t: string): boolean {
  const m = new Map();
  for (let i = 0; i < s.length; i++) {
    if (!m.has(s[i]))
      m.set(s[i], t[i]);
    else {
      if (m.get(s[i]) !== t[i])
        return false;
    }
  }
  return true;
}

const t = 'paper';
const s = 'title';
const res = isIsomorphic(t, s);
console.log(res);
