ackage main
import "fmt"
func sortDesc(arr [5]int) [5]int {
   for i := 0; i < len(arr); i++ {
   for j := 1 + i; j < len(arr); j++ {
         if arr[i] < arr[j] {
            intermediate := arr[i]
            arr[i] = arr[j]
            arr[j] = intermediate
         }
      }
   }
   return arr
}
func main() {
   arr := [5]int{50, 30, 20, 10, 40}
   fmt.Println("The unsorted array entered is:", arr)
   array := sortDesc(arr)
   fmt.Println()
   fmt.Println("The final array obtained after sorting is:", array)
}
