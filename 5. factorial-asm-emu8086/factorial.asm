mov ax, 5 ;factorial number (!5)

;the result is stored in the stack

mov bx,0


mov cx,ax
dec cx 

mov dx,ax


cmp dx,1


ja process:
       
jmp end   




process: 

    
    cmp dx,1  
    
    ja do
    
    jmp end
    
    
    do:
    
     
        push cx
        cyc:
            
            add bx,ax
            
        LOOP cyc
        
        
        
        mov ax,bx
        mov bx,0
        
        
        pop cx
        dec cx
        
        dec dx
        
        jmp process


end:
    push ax