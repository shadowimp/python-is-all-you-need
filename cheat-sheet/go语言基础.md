## go 语言

1. go 不需要写分号

2. 定义必须调用，引用必须调用

3. 需声明变量类型

   ```go
   var num int 
   ```

   - int   整型 , int 还有int8， iny16 ， int32， int64，

   - uint 无符号整型。 
   - %p 打印地址

4. 所有的调用必须要在主函数中

5. 打印与键盘输入语句

   ```go
   import "fmt"
   fmt.Println("")  // PrintLn 打印之后换行 ， 
   fmt.Scan()
   fmt.Scanln() // 读取一行
   ```

6. 数据类型

```go
var flag bool
flag = true 
fmt.Printf("%T,%t\n",flag,flag) // bool 类型 为 %t , %T用于查看变量类型

s1 = "shabi"
fmt.Print("%s",s1) 
```



7. 逻辑运算符 

   &&  与   ， || 或   ，  ！非

8. 条件语句 ： else if

   ```go
   if a == 1 || b==2{
     fmt.Print('a')
   }
   ```

   

9. For 语句

   ```go
   for i:=1 ; i <= 5 ; i++ {
     fmt.Println(i)
   }
   
   i := 1  
   for i <=5 {
     fmt.Println(i)
     i++ 
   }
   ```

10. 随机数

    ```go
    rand.Intn(10)
    ```

11. Array 

    ```go
    var nums [10] int32 
    nums = append(nums, 1)  // 添加元素,nums.append(1)
    l = l[:len(l)-1]  // l.pop()
    ```

    定义数组时定义长度，默认值为0。

12. 字典

    ```go
    var map1 = map[int]int{}
    ```

    ```go
    map2 = make(map[int]string)
    
    dic := map[uint8]uint8{
            '(':')',
            '{':'}',
            '[':']',
        }
    ```

    

### 函数

需要声明，函数名 ， input类型， output类型, 函数内容

声明括号里面写input形参及变量类型， 括号外写output类型

```go
func fun(a1 int, a2 int)int{
  b = a1+ a2
  return a1+a2
}

func max(x int , y int)int{
  if x>y{
    return x
  }else{
    return y
  }
}
```

### 打开文件

```go		
file, err := os.Open("test.txt")
if err != nil{
  panic(err)
}
defer file.Close()
scanner := bufio.NewScanner(file)
或者
rd := bufio.NewReader(file)

for scanner.Scan(){
  fmt.Println(strings.TrimSpace(scanner.Text))
}



```

### defer 延迟语句 ， 在函数最后执行

1. defer 先传递参数， 最后执行
2. 常用于文件读写



### 读 json数据

```go
import "encoding/json"
file, err := os.Open("test.txt")
if err != nil{
  painc(err)
}
defer file.Close()

var map1 = map[string][string]
decoder := json.NewDecoder(file)
err = decoder.Decode(&person)
if err != nil{
  panic(err)
}else{
  fmt.Println(person)
}
```

### strings

TrimSpace， 去除字符串前后端空格。

```go
line = strings.TrimSpace(line)
```