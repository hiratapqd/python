Attribute VB_Name = "Module1"
Sub Button1_Click()
'botao lets rock
find_first_last
dados_iniciais_finais
alimentando_dashboard
End Sub


Sub antigo_Button1_Click()
'botao lets rock
Sheets("Sheet1").Activate
Dim lastrow As Long

b = 260

'Incluir colunas compressao e savings
If ActiveSheet.Cells(9, 7) <> "savings" Then
    ActiveSheet.Range("f:g").EntireColumn.Insert
    ActiveSheet.Cells(9, 6) = "compression"
    ActiveSheet.Cells(9, 7) = "savings"
    ActiveSheet.Columns("f:f").Select
    Selection.NumberFormat = "0.00%"
End If
For i = 10 To 260
    If ActiveSheet.Cells(i, 1) <> "" Then
    ActiveSheet.Cells(i, 6) = (ActiveSheet.Cells(i, 4) - ActiveSheet.Cells(i, 5)) / ActiveSheet.Cells(i, 4)
     ActiveSheet.Cells(i, 7) = ActiveSheet.Cells(i, 4) - ActiveSheet.Cells(i, 5)
    Else: i = b
    End If
Next i

'identificando servidores distintos
lastrow = Cells(Rows.Count, "B").End(xlUp).Row
ActiveSheet.Range("B10:B" & lastrow).AdvancedFilter _
Action:=xlFilterCopy, _
CopyToRange:=ActiveSheet.Range("n10"), _
Unique:=True
For i = 11 To lastrow
    If ActiveSheet.Cells(i, 14) <> "" Then
    ActiveSheet.Range("o10:aa10").Copy
    ActiveSheet.Cells(i, 15).Select
    ActiveSheet.Paste
    Application.CutCopyMode = False
    End If
    
Next i

' quantas vezes os servidores foram backpeados
m = 9
For l = 10 To b
    If ActiveSheet.Cells(l, 14) <> "" Then
    m = m + 1
    Else: l = b
    End If
Next l

For g = 10 To m
' dados iniciais
For h = 10 To b
    If ActiveSheet.Cells(h, 1) <> "" Then
        If ActiveSheet.Cells(h, 1) = ActiveSheet.Cells(g, 16) And ActiveSheet.Cells(h, 2) = ActiveSheet.Cells(g, 14) Then
            ActiveSheet.Cells(g, 17) = ActiveSheet.Cells(h, 10)
            ActiveSheet.Cells(g, 18) = ActiveSheet.Cells(h, 4)
            ActiveSheet.Cells(g, 19) = ActiveSheet.Cells(h, 5)
        End If
    Else: h = b
    End If
Next h
'dados finais
    For l = 10 To b
        If ActiveSheet.Cells(l, 1) = ActiveSheet.Cells(g, 20) And ActiveSheet.Cells(l, 2) = ActiveSheet.Cells(g, 14) Then
            ActiveSheet.Cells(g, 21) = ActiveSheet.Cells(l, 10)
            ActiveSheet.Cells(g, 22) = ActiveSheet.Cells(l, 4)
            ActiveSheet.Cells(g, 23) = ActiveSheet.Cells(l, 5)
        End If
    Next l
Next g
p = "n10:n" & m
q = "x10:aa" & m
r = "c2:c" & m

'copiando os dados para o dashboard
ActiveSheet.Range(p).Copy
Sheets("DashBoard").Activate
ActiveSheet.Cells(2, 1).Select
ActiveSheet.Paste
Worksheets("Sheet1").Activate
ActiveSheet.Range(q).Copy
Sheets("DashBoard").Activate
ActiveSheet.Cells(2, 2).Select
ActiveSheet.Cells(2, 2).PasteSpecial xlPasteValues
Sheets("Sheet1").Activate
ActiveSheet.Range("y10").Copy
Sheets("DashBoard").Activate
ActiveSheet.Cells(2, 3).Select
ActiveSheet.Range(r).PasteSpecial Paste:=xlPasteFormats

Sheets("DashBoard").Activate
y = 2
For l = 2 To m
    If ActiveSheet.Cells(l, 1) <> "" Then
    y = y + 1
    Else: l = m
    End If
Next l
w = "d2:d" & y
e = "e2:e" & y
v = "c" & y + 2 & ":f" & y + 4
c = "d2:e" & y
sumtotal = WorksheetFunction.Sum(Range(w))
sumtotal1 = WorksheetFunction.Sum(Range(e))
Worksheets("DashBoard").Cells(y + 2, 3) = "Sem Arcserve"
Worksheets("DashBoard").Cells(y + 2, 4) = sumtotal
Worksheets("DashBoard").Cells(y + 3, 3) = "Com Arcserve"
Worksheets("DashBoard").Cells(y + 3, 4) = sumtotal1
Worksheets("DashBoard").Cells(y + 4, 3) = "Efeito Arcserve"
Worksheets("DashBoard").Cells(y + 4, 4) = sumtotal - sumtotal1
'Worksheets("Sheet1").Range("A1:E1").Columns.AutoFit
Worksheets("DashBoard").Range(v).Columns.AutoFit
Worksheets("DashBoard").Range(v).Font.Bold = True
Worksheets("DashBoard").Range(v).NumberFormat = "#,###,##0.00"
Worksheets("DashBoard").Range(c).NumberFormat = "#,###,##0.00"

'Mudando o tempo de backup de dias para meses
Worksheets("DashBoard").Cells(1, 2) = "Months"
For i = 2 To y
If Worksheets("DashBoard").Cells(i, 1) <> "" Then
    Worksheets("DashBoard").Cells(i, 2) = ActiveSheet.Cells(i, 2) / 30
    Worksheets("DashBoard").Cells(i, 2).NumberFormat = "#,###,##0.00"
End If
Next i
Worksheets("DashBoard").Cells(1, 1).Select

End Sub

Sub find_first_last()

'calculando quando apareceu a primeira e ultima vez o servidor no backup
'find first
'=INDEX($A$10:$A$257,MATCH(N10,$B$10:$B$257,0))
'find last
'=LOOKUP(2;1/($B$10:$B$257=N10);$A$10:$A$17)
  Dim job As String
  Dim searchTerm As Range


'Worksheets("Sheet1").Range("p1:p3").Formula = "=INDEX($A$10:$A$257,MATCH(N10,$B$10:$B$257,0))"
'Worksheets("Sheet1").Range("t1:t3").Formula = "=LOOKUP(2;1/($B$10:$B$257=N10);$A$10:$A$17)"
For i = 10 To 10000

    r1 = "n" & i
    'MsgBox r1
    range1 = Worksheets("sheet1").Range("b10:b257")
    range2 = Worksheets("sheet1").Range("a10:a257")
    x1 = Worksheets("sheet1").Range(r1)
    If x1 <> "" Then
        'find first
        myvar1 = Application.WorksheetFunction.Match(x1, range1, 0)
        myvar2 = Application.WorksheetFunction.Index(range2, myvar1)
        r2 = "p" & i
        Worksheets("sheet1").Range(r2) = myvar2
        'find last
        job = ActiveSheet.Cells(i, 14)
        Set searchTerm = Range("b1:b9999").Find(what:=job, searchorder:=xlByColumns, SearchDirection:=xlPrevious)
        If searchTerm Is Nothing Then
           MsgBox "Text was not found"
        Else
        '    MsgBox "Last cell is " & searchTerm.Address
           a = Mid(searchTerm.Address, 4)
        '    MsgBox a
           b = "a" & a
           c = ActiveSheet.Range(b)
            ActiveSheet.Cells(i, 20) = ActiveSheet.Range(b)
        '    MsgBox c
        End If
    End If
    
Next i
End Sub


Sub DropDown4_click()
End Sub

Sub ListBox7_Click()
    
'    Dim i As Long
'    With ActiveSheet.ListBoxes("List Box 7")
'        For i = 1 To .ListCount
'            If .Selected(i) Then
'                MsgBox i 'item i selected
'            End If
'        Next i
'    End With
    Dim i As Long
    With ActiveSheet.Shapes("List Box 7").OLEFormat.Object
        For i = 1 To .ListCount
            If .Selected(i) Then
                'MsgBox .List(i) 'item i selected
                ActiveSheet.Range("ae1") = .List(i)
            End If
        Next i
    End With
get_distinct_server
End Sub

Sub dataextract()
'conecta no db e lista as empresas. esse modulo foi copiado para o thisworkbook
'Declare variables'
Set objMyConn = New ADODB.Connection
Set objMyCmd = New ADODB.Command
Set objmyrecordset = New ADODB.Recordset

'Open Connection'
objMyConn.ConnectionString = "Provider=SQLOLEDB;Data Source=aimbetter\sqlexpress;User ID=sa;Password=Solve123!;"
objMyConn.Open

'Set and Excecute SQL Command'
Set objMyCmd.ActiveConnection = objMyConn
objMyCmd.CommandText = "select distinct company from acmedb.dbo.archchk_tbl order by company asc"
objMyCmd.CommandType = adCmdText
objMyCmd.Execute

'Open Recordset'
Set objmyrecordset.ActiveConnection = objMyConn
objmyrecordset.Open objMyCmd

'Copy Data to Excel'
'    With ActiveSheet.ListBoxes("list box 7")"
'.RemoveAllItems
'         Do
'           .AddItem "Dog"
'            'objmyrecordset.MoveNext
'        Loop Until objmyrecordset.EOF
'    End With
ActiveSheet.Range("Ad1").CopyFromRecordset (objmyrecordset)
ActiveSheet.ListBoxes("list Box 7").RemoveAllItems
m = 1
For i = 1 To 200
If ActiveSheet.Cells(i, 30) <> "" Then
    ActiveSheet.ListBoxes("list Box 7").AddItem ActiveSheet.Cells(i, 30)
    m = m + 1
Else: i = 200
End If
Next i
l = "ad1:ad" & m
ActiveSheet.Range(l).Delete
End Sub

Sub get_distinct_server()

'Declare variables'
Set objMyConn = New ADODB.Connection
Set objMyCmd = New ADODB.Command
Set objmyrecordset = New ADODB.Recordset

'Open Connection'
objMyConn.ConnectionString = "Provider=SQLOLEDB;Data Source=aimbetter\sqlexpress;User ID=sa;Password=Solve123!;"
objMyConn.Open

'Set and Excecute SQL Command'
Set objMyCmd.ActiveConnection = objMyConn
objMyCmd.CommandText = "select distinct server from acmedb.dbo.archchk_tbl where company=" & "'" & ActiveSheet.Range("ae1") & "'"
objMyCmd.CommandType = adCmdText
objMyCmd.Execute

'Open Recordset'
Set objmyrecordset.ActiveConnection = objMyConn
objmyrecordset.Open objMyCmd
'Copy Data to Excel'
ActiveSheet.Range("ae2").CopyFromRecordset (objmyrecordset)
objMyConn.Close
m = 1
ActiveSheet.ListBoxes("list Box 8").RemoveAllItems
For i = 1 To 200
If ActiveSheet.Cells(i, 31) <> "" Then
    ActiveSheet.ListBoxes("list Box 8").AddItem ActiveSheet.Cells(i, 31)
    m = m + 1
Else: i = 200
End If
Next i
l = "ae1:ae" & m
ActiveSheet.Range("ae:ae").Delete
End Sub

Sub ListBox8_Click()
    Dim i As Long
    With ActiveSheet.Shapes("List Box 8").OLEFormat.Object
        For i = 1 To .ListCount
            If .Selected(i) Then
                'MsgBox .List(i) 'item i selected
                ActiveSheet.Range("af1") = .List(i)
                'ActiveSheet.Shapes("Label 9").TextFrame.Characters.Text = .List(i)
            End If
        Next i
    End With
'MsgBox ActiveSheet.Shapes("Label 9").TextFrame.Characters.Text
get_how_many_bkps
End Sub

Sub get_how_many_bkps()

'Declare variables'
Set objMyConn = New ADODB.Connection
Set objMyCmd = New ADODB.Command
Set objmyrecordset = New ADODB.Recordset

'Open Connection'
objMyConn.ConnectionString = "Provider=SQLOLEDB;Data Source=aimbetter\sqlexpress;User ID=sa;Password=Solve123!;"
objMyConn.Open

'Set and Excecute SQL Command'
Set objMyCmd.ActiveConnection = objMyConn
objMyCmd.CommandText = "select count (server) from acmedb.dbo.archchk_tbl where server=" & "'" & ActiveSheet.Range("af1") & "'"
objMyCmd.CommandType = adCmdText
objMyCmd.Execute

'Open Recordset'
Set objmyrecordset.ActiveConnection = objMyConn
objmyrecordset.Open objMyCmd
ActiveSheet.Range("af2").CopyFromRecordset (objmyrecordset)
'Copy Data to Excel'
'ActiveSheet.TextBox1.Text = ""
lion = "O servidor " & ActiveSheet.Range("af1") & " tem " & ActiveSheet.Range("af2") & " backups"
'ActiveSheet.Shapes("Label 9").TextFrame.Characters.Text = lion

Worksheets("sheet1").Label1.AutoSize = False
'Worksheets("sheet1").Label1.WordWrap = False
'Worksheets("sheet1").Label1.Width = 2000
Worksheets("sheet1").Label1.Caption = lion

objMyConn.Close

End Sub

Sub dados_iniciais_finais()
' quantas vezes os servidores foram backpeados
m = 9
b = 10000
For l = 10 To b
    If ActiveSheet.Cells(l, 14) <> "" Then
    g = "b" & l
    f = "o" & l
    s = "=countif($b$10:$b$10000," & g & ")"
    Worksheets("Sheet1").Range(f).Formula = s
    m = m + 1
    Else: l = b
    End If
Next l


For g = 10 To m
' dados iniciais
For h = 10 To b
    If ActiveSheet.Cells(h, 1) <> "" Then
        If ActiveSheet.Cells(h, 1) = ActiveSheet.Cells(g, 16) And ActiveSheet.Cells(h, 2) = ActiveSheet.Cells(g, 14) Then
            ActiveSheet.Cells(g, 17) = ActiveSheet.Cells(h, 10)
            ActiveSheet.Cells(g, 18) = ActiveSheet.Cells(h, 4)
            ActiveSheet.Cells(g, 19) = ActiveSheet.Cells(h, 5)
        End If
    Else: h = b
    End If
Next h
'dados finais
    For l = 10 To b
        If ActiveSheet.Cells(l, 1) = ActiveSheet.Cells(g, 20) And ActiveSheet.Cells(l, 2) = ActiveSheet.Cells(g, 14) Then
            ActiveSheet.Cells(g, 21) = ActiveSheet.Cells(l, 10)
            ActiveSheet.Cells(g, 22) = ActiveSheet.Cells(l, 4)
            ActiveSheet.Cells(g, 23) = ActiveSheet.Cells(l, 5)
        End If
    Next l
'calculos das diferencas
    ActiveSheet.Cells(g, 24) = ActiveSheet.Cells(g, 20) - ActiveSheet.Cells(g, 16)
    ActiveSheet.Cells(g, 25) = ActiveSheet.Cells(g, 21) - ActiveSheet.Cells(g, 17)
    ActiveSheet.Cells(g, 26) = ActiveSheet.Cells(g, 22) - ActiveSheet.Cells(g, 18)
    ActiveSheet.Cells(g, 27) = ActiveSheet.Cells(g, 23) - ActiveSheet.Cells(g, 19)
    

Next g




End Sub

Sub alimentando_dashboard()
m = 9
b = 10000
For l = 10 To b
    If ActiveSheet.Cells(l, 14) <> "" Then
    m = m + 1
    Else: l = b
    End If
Next l
p = "n10:n" & m
q = "x10:aa" & m
r = "c2:c" & m
Worksheets("Sheet1").Activate
'copiando os dados para o dashboard
ActiveSheet.Range(p).Copy
Sheets("DashBoard").Activate
ActiveSheet.Cells(2, 1).Select
ActiveSheet.Paste
Worksheets("Sheet1").Activate
ActiveSheet.Range(q).Copy
Sheets("DashBoard").Activate
ActiveSheet.Cells(2, 2).Select
ActiveSheet.Cells(2, 2).PasteSpecial xlPasteValues
Sheets("Sheet1").Activate
ActiveSheet.Range("y10").Copy
Sheets("DashBoard").Activate
ActiveSheet.Cells(2, 3).Select
ActiveSheet.Range(r).PasteSpecial Paste:=xlPasteFormats

Sheets("DashBoard").Activate
y = 2
For l = 2 To m
    If ActiveSheet.Cells(l, 1) <> "" Then
    y = y + 1
    Else: l = m
    End If
Next l
w = "d2:d" & y
e = "e2:e" & y
v = "c" & y + 2 & ":f" & y + 4
c = "d2:e" & y
sumtotal = WorksheetFunction.Sum(Range(w))
sumtotal1 = WorksheetFunction.Sum(Range(e))
Worksheets("DashBoard").Cells(y + 2, 3) = "Sem Arcserve"
Worksheets("DashBoard").Cells(y + 2, 4) = sumtotal
Worksheets("DashBoard").Cells(y + 3, 3) = "Com Arcserve"
Worksheets("DashBoard").Cells(y + 3, 4) = sumtotal1
Worksheets("DashBoard").Cells(y + 4, 3) = "Efeito Arcserve"
Worksheets("DashBoard").Cells(y + 4, 4) = sumtotal - sumtotal1
'Worksheets("Sheet1").Range("A1:E1").Columns.AutoFit
Worksheets("DashBoard").Range(v).Columns.AutoFit
Worksheets("DashBoard").Range(v).Font.Bold = True
Worksheets("DashBoard").Range(v).NumberFormat = "#,###,##0.00"
Worksheets("DashBoard").Range(c).NumberFormat = "#,###,##0.00"

'Mudando o tempo de backup de dias para meses
Worksheets("DashBoard").Cells(1, 2) = "Months"
For i = 2 To y
If Worksheets("DashBoard").Cells(i, 1) <> "" Then
    Worksheets("DashBoard").Cells(i, 2) = ActiveSheet.Cells(i, 2) / 30
    Worksheets("DashBoard").Cells(i, 2).NumberFormat = "#,###,##0.00"
End If
Next i
Worksheets("DashBoard").Cells(1, 1).Select
End Sub
