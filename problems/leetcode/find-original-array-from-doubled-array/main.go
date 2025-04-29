/*
issue
    original    changed (doubled)
    [1,3,4]  <-  [1,3,4,2,6,8]
    ---
    derive original out of changed
        issue
            determine doubled-ness
                condition
					number of 
                    changed.length % 2 == 0 && check 
            remove doubled elems from changed

solution
    if changed.length % 2 == 0
        deriveOriginal()
    else
        return []

changed
    properties
        even nums of elems
            examples
                1,3 -> 1,3,2,6
                1,5,3,5 -> 1,5,3,5,2,10,6,10
*/
package main
func findOriginalArray(changed []string)
func main() {
	changed := [1,3,4,2,6,8]

	findOriginalArray(changed)
}
