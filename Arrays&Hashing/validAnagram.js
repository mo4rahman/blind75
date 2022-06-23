function validAnagram(s, t) {
  if (s.length !== t.length) {
    return false;
  }
  for (let i = 0; i < s.length; i++) {
    if (t.includes(s[i])) {
      continue;
    } else {
      return false;
    }
  }

  for (let i = 0; i < t.length; i++) {
    if (s.includes(t[i])) {
      continue;
    } else {
      return false;
    }
  }

  return true;
}

console.log(validAnagram("car", "rat")); // false
console.log(validAnagram("amard", "draaa")); // false
console.log(validAnagram("amard", "drama")); // true



