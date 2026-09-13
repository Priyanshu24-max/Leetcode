class Solution:
    def defangIPaddr(self, address: str) -> str:
        add_list=list[str](address)

        new=[str("[.]") if x=="." else x for x in add_list] #if x=="." then replace it with "[.]"
        return "".join(new)
        